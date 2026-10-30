#!/usr/bin/env python3
"""star_velocity.py -- the instrument Gap 549-E demanded (p550).

WHY THIS EXISTS
  p549 registered Gap 549-E against the trending channel: every "AI trends"
  feed this base can reach trades in star VELOCITY ("+2 371 stars today"),
  and this base had an instrument for a star LEVEL only. It could therefore
  neither confirm nor refute the one quantity the feeds actually sell.

  p549 also named the fix, and named it correctly:

      "The cheap fix is this base's own history: `git log` over its published
       figures already IS a time series, at pass granularity -- DeepTutor
       moved 49 850 -> 51 247 between p537 and p549. So velocity is derivable
       from the base itself and does NOT require the channel the feeds use."

  This is that instrument. It does not call GitHub. It reads the committed
  bytes of this repository's own shelf pages and reconstructs, per address,
  the series of star figures this base has published over its own history.

WHAT IT GUARANTEES
  1. NO NETWORK. The series is derived from `git log` + `git show` only, so it
     is reproducible offline and cannot be contradicted by a channel outage.
     Gap 547-E took two passes off this base; a history instrument is immune.
  2. THE RULE TRAVELS WITH THE FIGURE (Gap 549-B). Every output row carries
     RULE_NAME/RULE_REV. Changing the extraction is a diff, not a recollection.
  3. UNPARSED IS NOT ZERO (Gap 549-A one level down). A declared star cell
     this base published as `UNREAD`, `--` or prose is emitted as UNPARSED
     with the raw cell preserved -- never as 0, never silently dropped.
  4. VELOCITY CARRIES ITS WINDOW. A delta over 12 days and a delta over 1 day
     are not the same measurement, so `days` always prints beside `delta` and
     `per_day` is blank when the window is 0 days.
  5. INTRA-COMMIT DISAGREEMENT IS A RESULT, NOT A TIE TO BREAK. If one commit
     publishes two different figures for one address, BOTH are emitted and
     marked SPLIT. This is the instrument's highest-value output: it is how
     p549's own defect -- a shelf row reading 49 850 beside a re-attestation
     table reading 51 247, in the same commit -- is found mechanically
     instead of by hand.

RULE
  declared_star_cell / rev4
    A star claim is a table row that (a) contains `github.com/<owner>/<repo>`
    and (b) sits in a table whose header row DECLARES a Stars column. The
    header is located as the row immediately above the `|---|` delimiter, so
    it resets at every table and no table can inherit another's column index.

    THERE IS NO POSITIONAL FALLBACK, BY DESIGN. rev3 had one and it was wrong:
    on this base's own pages it returned 11 408 for DeepTutor at p521 by
    picking a number out of a narrative table that has no Stars column at all.
    A table that does not declare stars is not making a star claim, and
    guessing which of its cells meant stars manufactures data. Silence from a
    non-stars table is correct silence.

    Cell -> value: the cell is CUT at the first `·` (the delimiter between the
    star figure and the fork figure on these pages), then emphasis, emoji and
    any `N forks/commits/issues` tail are stripped, then digit-group
    separators -- including U+202F and U+2009, which appear INSIDE published
    figures such as `49 850` -- are removed, then:
        ^\\d+(\\.\\d+)?[kK]?$
    `41.8k` -> 41800, marked ROUNDED; p549 measured that rounded figures decay
    fastest, so precision is reported rather than discarded.

USAGE   ./star_velocity.py OWNER/REPO [OWNER/REPO ...]
OUTPUT  TSV: address pass date stars precision how delta days per_day rule
"""
import datetime
import re
import subprocess
import sys

RULE_NAME = "declared_star_cell"
RULE_REV = "rev5"

SHELF_PAGES = [
    "agents/top.md",
    "repos/foundations.md",
    "verticals/solutions.md",
    "compose/patterns.md",
]

# Digit-group separators used inside published figures on these pages.
# U+202F NARROW NO-BREAK SPACE and U+2009 THIN SPACE are the ones that matter:
# `49 850` is one number, and splitting on whitespace would make it two.
SEPS = "     ,"

EMPH = re.compile(r"[*_`]+")
# Deliberately narrow. A blanket "strip non-ASCII" would also eat the digit
# separators above -- which is the bug this comment exists to prevent.
GLYPHS = re.compile(r"[\U0001F300-\U0001FAFF☀-➿️]")
TAIL = re.compile(r"(forks?|commits?|issues?|stars?)\b.*$", re.I)
SCALAR = re.compile(r"^\d+(\.\d+)?[kK]?$")
DELIM = re.compile(r"^\|[\s:|-]+\|$")
STARS_HDR = re.compile(r"^\**\s*stars?\s*\**$", re.I)
PAREN = re.compile(r"\s*\([^)]*\)\s*$")


def sh(args):
    return subprocess.run(args, capture_output=True, text=True).stdout


def commits_touching(pages):
    """Oldest-first commits touching any shelf page: (sha, date, subject)."""
    out = sh(["git", "log", "--reverse", "--date=short",
              "--pretty=%H\t%ad\t%s", "--"] + pages)
    rows = []
    for ln in out.splitlines():
        parts = ln.split("\t", 2)
        if len(parts) == 3:
            rows.append(tuple(parts))
    return rows


def pass_of(subject):
    m = re.search(r"\bp(\d{2,5})\b", subject)
    return "p" + m.group(1) if m else "?"


def cells(row):
    r = row.strip()
    if r.startswith("|"):
        r = r[1:]
    if r.endswith("|"):
        r = r[:-1]
    return r.split("|")


def stars_index(header_row):
    """Index of the declared Stars column, or None."""
    for i, h in enumerate(cells(header_row)):
        h = GLYPHS.sub("", h).strip()
        if STARS_HDR.match(h):
            return i
    return None


def to_stars(cell):
    """(value, precision) or (None, raw). Prose never becomes a number."""
    raw = cell.strip()
    c = raw.split("·")[0]
    c = EMPH.sub("", c)
    c = GLYPHS.sub("", c)
    c = TAIL.sub("", c)
    # A trailing parenthetical annotation is a note ABOUT the figure, not part
    # of it: these pages publish `50.5k *(rounded)*` and `44 177 (re-measured)`.
    # Without this, such a cell reads as prose and the figure is lost as
    # UNPARSED -- which hid a cross-page disagreement on the largest row here.
    c = PAREN.sub("", c)
    c = c.strip()
    for s in SEPS:
        c = c.replace(s, "")
    if not c or not SCALAR.match(c):
        return None, raw
    if c[-1] in "kK":
        return int(round(float(c[:-1]) * 1000)), "ROUNDED"
    if "." in c:
        return None, raw
    return int(c), "EXACT"


def claims_on_page(blob, pat):
    """Every declared star claim for `pat` on one page blob."""
    out = []
    lines = blob.splitlines()
    idx = None
    for i, ln in enumerate(lines):
        s = ln.strip()
        if not s.startswith("|"):
            continue
        # Reset at every table: the header is the row above the delimiter.
        if i + 1 < len(lines) and DELIM.match(lines[i + 1].strip()):
            idx = stars_index(s)
            continue
        if idx is None or not pat.search(s):
            continue
        cs = cells(s)
        if idx >= len(cs):
            continue
        # rev5, IDENTITY-COLUMN CONSTRAINT. The address must appear in a cell
        # BEFORE the Stars column -- i.e. in the row's identity columns (name,
        # repo), not in its trailing prose.
        #
        # rev4 lacked this and was WRONG in a way that manufactured a defect:
        # `repos/foundations.md` carries a row for `CAHLR/pyBKT` (291 stars)
        # whose description reads "the same lab behind [OATutor](...)". rev4
        # matched that row for `CAHLR/OATutor` and attributed pyBKT's 291 to
        # OATutor, then -- because OATutor's own row says 274 -- reported a
        # SPLIT and accused this base of publishing two figures for one repo.
        # The base was right; the rule was wrong. pyBKT measures 291 exactly.
        #
        # On every shelf layout here the identity columns precede Stars
        # (`| Agent | Repo | Licence | Stars | ...`, `| Repo | Licence | Stars
        # | ...`), so "before the stars column" is the portable spelling of
        # "is this row ABOUT the address, or does it merely CITE it".
        if not any(pat.search(c) for c in cs[:idx]):
            continue
        v, p = to_stars(cs[idx])
        out.append((v, p))
    return out


def series_for(address, commits):
    pat = re.compile(r"github\.com/" + re.escape(address) + r"(?![\w/-])", re.I)
    rows = []
    for sha, date, subject in commits:
        found = []
        for page in SHELF_PAGES:
            blob = sh(["git", "show", f"{sha}:{page}"])
            if blob and pat.search(blob):
                found += claims_on_page(blob, pat)
        if not found:
            continue
        vals = {v for v, _ in found if v is not None}
        split = len(vals) > 1
        seen = set()
        for v, p in found:
            key = (v, p)
            if key in seen:
                continue
            seen.add(key)
            rows.append({"pass": pass_of(subject), "date": date, "stars": v,
                         "precision": p, "split": split})
    # Collapse a figure republished unchanged: the series records CHANGES.
    out = []
    for r in rows:
        if (out and out[-1]["stars"] == r["stars"]
                and out[-1]["precision"] == r["precision"] and not r["split"]):
            continue
        out.append(r)
    return out


def summarise(address, ser):
    """One row per address: span, net move, and CURRENT split state.

    The per-commit series is deliberately verbose -- a SPLIT re-emits on every
    commit it survives, because "this disagreement has stood for six passes" is
    the finding, not noise. This view is what a pass reads before deciding
    where to spend its re-measurement budget.
    """
    fmt = "%Y-%m-%d"
    parsed = [r for r in ser if r["stars"] is not None]
    if not parsed:
        return None
    first, last = parsed[0], parsed[-1]
    days = (datetime.datetime.strptime(last["date"], fmt)
            - datetime.datetime.strptime(first["date"], fmt)).days
    net = last["stars"] - first["stars"]
    # "Frozen" = the published figure has not moved since this pass, which is a
    # staleness candidate, NOT a claim the upstream repo stopped growing.
    frozen_since = last["pass"]
    for r in reversed(parsed):
        if r["stars"] != last["stars"]:
            break
        frozen_since = r["pass"]
    cur_split = sorted({r["stars"] for r in ser
                        if r["split"] and r["date"] == last["date"]
                        and r["stars"] is not None})
    return {
        "address": address, "obs": len(parsed),
        "first": f'{first["stars"]}@{first["pass"]}',
        "last": f'{last["stars"]}@{last["pass"]}',
        "days": days, "net": net,
        "per_day": f"{net/days:.1f}" if days else "",
        "frozen_since": frozen_since,
        "split_now": "/".join(str(v) for v in cur_split) if len(cur_split) > 1 else "",
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    summary = "--summary" in sys.argv
    if not args:
        print("usage: star_velocity.py [--summary] OWNER/REPO [OWNER/REPO ...]",
              file=sys.stderr)
        sys.exit(2)
    commits = commits_touching(SHELF_PAGES)
    if summary:
        cols = ["address", "obs", "first", "last", "days", "net", "per_day",
                "frozen_since", "split_now"]
        print("\t".join(cols + ["rule"]))
        for address in args:
            row = summarise(address, series_for(address, commits))
            if row is None:
                print("\t".join([address, "0"] + [""] * 7
                                 + [f"{RULE_NAME}/{RULE_REV}"]))
                continue
            print("\t".join([str(row[c]) for c in cols]
                             + [f"{RULE_NAME}/{RULE_REV}"]))
        return
    print("\t".join(["address", "pass", "date", "stars", "precision", "how",
                     "delta", "days", "per_day", "rule"]))
    fmt = "%Y-%m-%d"
    for address in args:
        prev = None
        for r in series_for(address, commits):
            delta = days = per_day = ""
            if r["stars"] is not None and prev is not None and not r["split"]:
                delta = r["stars"] - prev["stars"]
                days = (datetime.datetime.strptime(r["date"], fmt)
                        - datetime.datetime.strptime(prev["date"], fmt)).days
                per_day = f"{delta/days:.1f}" if days else ""
            print("\t".join([
                address, r["pass"], r["date"],
                str(r["stars"]) if r["stars"] is not None else "UNPARSED",
                r["precision"] if r["stars"] is not None
                else f"RAW({str(r['precision'])[:40]})",
                "SPLIT" if r["split"] else "declared",
                str(delta), str(days), str(per_day),
                f"{RULE_NAME}/{RULE_REV}",
            ]))
            if r["stars"] is not None and not r["split"]:
                prev = r


if __name__ == "__main__":
    main()
