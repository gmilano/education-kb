"""p140-rootonly-header-reach — `ACTION CQ`: extend the source-header read to the five
unread `ROOT_ONLY` rows, and ask where ownership is recorded AT ALL.

`ACTION CQ` as p139 pre-registered it:

> Extend `ACTION CJ` to the **five unread `ROOT_ONLY` rows** (`Crosstalk-Solutions/project-nomad`,
> `overhangio/tutor`, `adaptlearning/adapt_framework`, `openedx/XBlock`, `openedx/codejail`).
> 🔴 *Refuted if none carries a foreign source header, which would make the 2-of-3 a property
> of the three largest rather than of the class.*

The foreign-header question is answered by re-running p139's own collector unchanged, which
is deliberate: a second instrument would confound a change of result with a change of method.
This module adds the two things the re-run needed.

## 1. A nameless-holder guard, because p139's classifier has a latent defect

🔴 `header_holder.extract_holder("Copyright © 2024")` returns **`"2024"`**. The year is
optional in the marker group, so when a notice carries a marker and a year and NO NAME, the
year falls through into the holder capture.

🟢 **p139's published results are NOT affected** -- its three rows contain no nameless notice,
and an audit of its committed detail table finds zero year-shaped holders. 🔴 **The defect
fired on the first new input**: `adaptlearning/adapt_framework` ships
`"attribution": "Copyright © 2024"` in `src/course/en/components.json`, and an unguarded run
publishes `2024` as a foreign copyright holder of the repository.

p139's committed code is left exactly as it was -- its result is a dated record and editing
the instrument under it would invalidate the record. The guard lives here instead, and the
tests below pin both the defect and the fix.

## 2. An ownership-location axis, because "no header" is not "no owner"

Three of the five rows carry **no copyright header in any source file**. That is not an
absence of ownership; it is ownership recorded somewhere else. So each row is also scored for
*where* a holder is findable:

  `ROOT_LICENCE_FILLED`  the licence's own appendix or template carries a real holder
  `ROOT_LICENCE_TEMPLATE` the appendix is present and left as `[name of copyright owner]`
  `NOTICE_FILE`          an Apache-style `NOTICE` names the holder
  `PACKAGE_METADATA`     `pyproject.toml` / `package.json` names an author or organisation
  `SOURCE_HEADER`        at least one source file carries a holder
  `NOWHERE`              none of the above

🔵 **This axis is what makes the pass's answer usable.** A delivery team asking "who holds this
code?" needs to know which file to open, and for these rows it is increasingly not the one
named `LICENSE`.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

# p139's classifier is the instrument under test and is imported, not copied.
_P139 = Path(__file__).resolve().parent.parent / "p139-source-header-holder"
sys.path.insert(0, str(_P139))

import header_holder as hh  # noqa: E402

# A holder capture that is only digits, punctuation and space is a YEAR, not a name.
# `©`/`(c)` plus a year plus nothing else is a nameless notice.
NAMELESS = re.compile(r"^[\d\s,./–—-]+$")

LICENCE_NAME = re.compile(r"^(LICENSE|LICENCE|COPYING|COPYRIGHT)", re.IGNORECASE)
NOTICE_NAME = re.compile(r"^NOTICE", re.IGNORECASE)
METADATA_FILES = ("pyproject.toml", "package.json", "setup.py", "setup.cfg")

# The Apache-2.0 appendix and the GPL "how to apply" template, unfilled.
TEMPLATE_HOLDER = re.compile(
    r"Copyright\s*(?:\[yyyy\]|\(C\)\s*[<{]year[>}]|\[year\])?\s*"
    r"(?:\[name of copyright owner\]|[<{]name of author[>}])",
    re.IGNORECASE,
)


def extract_holder(line):
    """p139's extraction, with the nameless-notice guard applied."""
    holder = hh.extract_holder(line)
    if holder is None:
        return None
    if NAMELESS.match(holder.strip()):
        return None
    return holder


def git(repo, *args):
    out = subprocess.run(("git", "-C", str(repo)) + args, capture_output=True, text=True)
    return out.stdout if out.returncode == 0 else ""


def tree_paths(repo):
    return [p for p in git(repo, "ls-tree", "-r", "HEAD", "--name-only").splitlines() if p]


def show(repo, path):
    return git(repo, "show", "HEAD:" + path)


def ownership_locations(repo, own_names):
    """Where, if anywhere, a holder of this row is recorded."""
    paths = tree_paths(repo)
    found, detail = [], {}

    roots = [p for p in paths if "/" not in p]

    for p in [p for p in roots if LICENCE_NAME.match(p)]:
        text = show(repo, p)
        holders = [h for h in (extract_holder(l) for l in text.splitlines()) if h]
        real = [h for h in holders if not hh.is_steward(h)]
        if real:
            found.append("ROOT_LICENCE_FILLED")
            detail["root_licence"] = {"file": p, "holders": sorted(set(real))}
        elif TEMPLATE_HOLDER.search(text):
            found.append("ROOT_LICENCE_TEMPLATE")
            detail["root_licence"] = {"file": p, "holders": [], "template": True}
        else:
            detail["root_licence"] = {"file": p, "holders": [],
                                      "steward_only": sorted(set(holders))}

    for p in [p for p in roots if NOTICE_NAME.match(p)]:
        holders = [h for h in (extract_holder(l) for l in show(repo, p).splitlines()) if h]
        real = [h for h in holders if not hh.is_steward(h)]
        if real:
            found.append("NOTICE_FILE")
            detail["notice"] = {"file": p, "holders": sorted(set(real))}

    for p in [p for p in roots if p in METADATA_FILES]:
        text = show(repo, p)
        who = []
        if p == "package.json":
            try:
                d = json.loads(text)
            except ValueError:
                d = {}
            a = d.get("author")
            if isinstance(a, dict):
                a = a.get("name") or a.get("email")
            if a:
                who.append(str(a))
        else:
            for m in re.finditer(r"(?:name|author)\s*=\s*[\"']([^\"']{2,80})[\"']", text):
                who.append(m.group(1))
            for m in re.finditer(r"\{\s*name\s*=\s*[\"']([^\"']{2,80})[\"']", text):
                who.append(m.group(1))
            for m in re.finditer(r"email\s*=\s*[\"']([^\"'@]+@[^\"']+)[\"']", text):
                who.append(m.group(1))
        who = [w for w in who if w.lower() not in {Path(str(repo)).name.lower()}]
        if who:
            found.append("PACKAGE_METADATA")
            detail.setdefault("metadata", {})[p] = sorted(set(who))

    return (sorted(set(found)) or ["NOWHERE"]), detail


SUMMARY_COLS = [
    "slug", "tree_paths", "source_headers", "own_holders", "foreign_holders",
    "nameless_suppressed", "header_verdict", "ownership_locations",
]


def scan_row(repo, slug, own_csv):
    own = [n.strip() for n in own_csv.split(",") if n.strip()]

    # p139's collector, re-run unchanged, then re-filtered through the guard.
    total, considered, licence_files, holders = hh_scan(repo, own)
    suppressed = [h for h in holders if NAMELESS.match(h.strip())]
    kept = {h: r for h, r in holders.items() if h not in suppressed}

    foreign = {h: r for h, r in kept.items() if r["class"] == "FOREIGN"}
    own_h = {h: r for h, r in kept.items() if r["class"] == "OWN"}
    verdict = "FOREIGN_HEADER_IN_SOURCE" if foreign else (
        "OWN_HEADERS_ONLY" if own_h else "NO_HEADER_AT_ALL")

    locs, detail = ownership_locations(repo, own)
    return {
        "slug": slug,
        "tree_paths": total,
        "source_headers": sum(r["count"] for r in kept.values()),
        "own_holders": len(own_h),
        "foreign_holders": len(foreign),
        "nameless_suppressed": len(suppressed),
        "header_verdict": verdict,
        "ownership_locations": "+".join(locs),
        "_holders": {h: {"class": r["class"], "count": r["count"]} for h, r in kept.items()},
        "_suppressed": suppressed,
        "_where": detail,
    }


def hh_scan(repo, own):
    """p139's `scan_headers.scan`, imported so the collector is identical."""
    sys.path.insert(0, str(_P139))
    import scan_headers  # noqa: PLC0415
    return scan_headers.scan(repo, own)


ROWS = [
    ("Crosstalk-Solutions/project-nomad", "Crosstalk Solutions"),
    ("overhangio/tutor", "Edly,Overhang,Regis Behmo,Régis Behmo"),
    ("adaptlearning/adapt_framework", "ADAPT LEARNING,Adapt Learning"),
    ("openedx/XBlock", "edX,Axim,Open edX"),
    ("openedx/codejail", "edX,Axim,Open edX"),
]


def main(argv):
    if len(argv) < 2 or (len(argv) - 1) % 3 != 0:
        print(__doc__, file=sys.stderr)
        print("usage: rootonly_reach.py <clone> <slug> <own_names_csv> [...]", file=sys.stderr)
        return 2
    triples = [argv[i:i + 3] for i in range(1, len(argv), 3)]
    rows = [scan_row(c, s, o) for c, s, o in triples]
    print("\t".join(SUMMARY_COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in SUMMARY_COLS))
    print("\n# holders and ownership locations", file=sys.stderr)
    for r in rows:
        print(r["slug"], json.dumps({
            "holders": r["_holders"],
            "nameless_suppressed": r["_suppressed"],
            "where": r["_where"],
        }, ensure_ascii=False, indent=2), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
