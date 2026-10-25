"""`Gap 434-A` / `Gap 434-B` — the promotion predicate that survives its own population.

`p434` built `gate-promotion` on a 7-row grade table, where `PERMISSIVE and absent from
every curated shelf` fired twice and looked like a defect detector.  `p435` completed the
grade table — all **2 450** unpromoted addresses, every grant read first-hand off
`raw.githubusercontent.com` — and the same predicate fires **1 449** times, **59.1 %** of
the population.

🔴 A predicate that selects the majority of its population is a CLASSIFIER OF THAT
POPULATION, not a defect detector.  Permissiveness is the backlog's ordinary property, so
it cannot be the whole promotion test.

🟢 The missing conjunct is RECENCY, and the reason to prefer it over `Gap 433-A`'s star
threshold is not taste — it is the only one of the two that a `make` target can obtain:

    git clone --depth 1 --bare --filter=tree:0 https://github.com/<slug>

costs ~0.5 s and ~270 KB (measured p435, against ~20 MB for a plain `--depth 1`) and
yields the HEAD commit object, hence its committer date AND its timezone offset — the
same offset channel `gate-offset-region` already places regions with.

`PERMISSIVE` is IMPORTED from `p444-root-vs-tree-family` and the population from
`p434-promotion-gate`, never restated — T108.

    recency.py classify <grades.tsv> [--days N] [--today YYYY-MM-DD]
    recency.py buckets  <grades.tsv> [--today YYYY-MM-DD]
"""
import csv
import datetime
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "p444-root-vs-tree-family"))
from root_vs_tree import PERMISSIVE                      # noqa: E402

# The window is not a taste.  `p435` measured the backlog's recency distribution and
# 0-30d is the one bucket whose members are, without exception, projects with a commit
# inside the current month -- which is what "live" means for a build-on recommendation.
DEFAULT_DAYS = 30

BUCKETS = ((30, "0-30d"), (90, "31-90d"), (180, "91-180d"),
           (365, "181-365d"), (730, "1-2y"), (None, ">2y"))


def age_days(iso_date, today):
    """`YYYY-MM-DD` -> whole days before `today`.  Negative ages are NOT clamped: a
    future committer date is a datum about the repository, not about this code."""
    d = datetime.date.fromisoformat(iso_date)
    return (today - d).days


def bucket(days):
    for edge, name in BUCKETS:
        if edge is None or days <= edge:
            return name
    raise AssertionError("unreachable: BUCKETS ends in None")


def read_grades(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def classify(rows, today, days=DEFAULT_DAYS):
    """-> (slate, rejected) over a completed grade table.

    A row joins the slate when it is PERMISSIVE *and* its HEAD commit is within `days`.
    An undated permissive row is `NO-DATE` and is never a slate row and never a defect:
    it is the reach bound of the recency channel, stated the way `p228` states one."""
    slate, rejected = [], []
    for r in rows:
        slug = r["slug"]
        fam = r.get("family", "")
        if fam not in PERMISSIVE:
            rejected.append((slug, fam, "-", "NOT-PERMISSIVE"))
            continue
        hd = r.get("head_committed", "-")
        if not hd or hd == "-":
            rejected.append((slug, fam, "-", "NO-DATE"))
            continue
        a = age_days(hd, today)
        if a <= days:
            slate.append((slug, fam, hd, r.get("tz_offset", "-"), a))
        else:
            rejected.append((slug, fam, hd, "STALE-" + bucket(a)))
    return slate, rejected


def main(argv):
    if not argv or argv[0] not in ("classify", "buckets"):
        sys.stderr.write(
            "p435-promotion-sweep: no mode given — refusing to judge a promotion "
            "surface over nothing\n"
            "usage: recency.py [classify|buckets] <grades.tsv> "
            "[--days N] [--today YYYY-MM-DD]\n")
        return 2
    mode, rest = argv[0], argv[1:]
    days, today, path = DEFAULT_DAYS, datetime.date.today(), None
    i = 0
    while i < len(rest):
        if rest[i] == "--days":
            days = int(rest[i + 1]); i += 2
        elif rest[i] == "--today":
            today = datetime.date.fromisoformat(rest[i + 1]); i += 2
        else:
            path = rest[i]; i += 1
    if not path:
        sys.stderr.write("p435-promotion-sweep: no grade table given — refusing\n")
        return 2
    rows = read_grades(path)
    if not rows:
        sys.stderr.write("p435-promotion-sweep: empty grade table — refusing (P541)\n")
        return 2
    slate, rejected = classify(rows, today, days)
    if mode == "buckets":
        counts = {}
        for r in rows:
            hd = r.get("head_committed", "-")
            key = "NO-DATE" if (not hd or hd == "-") else bucket(age_days(hd, today))
            fam = "PERMISSIVE" if r.get("family") in PERMISSIVE else "non-permissive"
            counts[(fam, key)] = counts.get((fam, key), 0) + 1
        print("arm\tbucket\tn")
        for (fam, key), n in sorted(counts.items()):
            print(f"{fam}\t{key}\t{n}")
        print(f"#\tpopulation\t{len(rows)}")
        return 0
    print("slug\tfamily\thead_committed\ttz_offset\tage_days")
    for row in sorted(slate, key=lambda r: (r[4], r[0])):
        print("\t".join(str(x) for x in row))
    print(f"#\tslate\t{len(slate)}\twindow={days}d")
    print(f"#\trejected\t{len(rejected)}\tREACH-AND-STALENESS-not-a-defect-count")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
