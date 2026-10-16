#!/usr/bin/env python3
"""Controls for p239-query-shape.

Every threshold control is anchored on a harvest actually run in p239 and recorded in
evidence/p239-query-shape.2026-10-16-p239.tsv, so the suite is a regression test
against measurement rather than against a chosen constant.

Runs from its own directory AND under `-I` from the repository root (p355-cwd-portability,
the defect that kept p229's gate a one-off).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from query_shape import (  # noqa: E402
    classify,
    is_harvestable,
    supports_absence,
    supports_recency,
    has_scope,
    CAUTION_MAX,
    REFUSE_MIN,
)

FAIL = []
N = 0


def check(label, got, want):
    global N
    N += 1
    if got != want:
        FAIL.append(f"{label}: got {got!r}, want {want!r}")


# ---------------------------------------------------------------- the six measured harvests
# (total_count, sort, query, measured on-topic %, expected verdict)
MEASURED = [
    (24, "updated", "org:Ed-Fi-Alliance-OSS pushed:>2026-01-01", 91.7, "SCOPED"),
    (253, "updated", "OneRoster in:name,description,readme pushed:>2026-04-01", 63.3, "SAMPLE"),
    (2326, "updated", "ClassLink OR state longitudinal data OR SIS integration", 2.5, "SLICE"),
    (7576, "stars", '"OneRoster" OR "Ed-Fi" OR "PowerSchool" in:name,description', 48.0, "HEAD"),
    (8618, "updated", "Ed-Fi in:name,description,readme pushed:>2026-04-01", 0.0, "SLICE"),
    (81905, "updated", "agente educativo OR tutor inteligente OR gestion escolar", 0.0, "SLICE"),
]

for total, sort, query, rate, want in MEASURED:
    verdict, _ = classify(total, sort, query)
    check(f"measured {total}@{sort} ({rate}% on-topic)", verdict, want)

# The gate must agree with the measurement about what was harvestable: every harvest
# that returned a readable page one is harvestable, every collapsed one is not.
for total, sort, query, rate, _ in MEASURED:
    verdict, _ = classify(total, sort, query)
    check(
        f"harvestable agrees with {rate}% at {total}@{sort}",
        is_harvestable(verdict),
        rate >= 40.0,
    )
    # Only the two harvests that were both narrow and recency-ordered may carry an
    # absence; the 48% stars harvest supplied rows but cannot say what is missing.
    check(
        f"absence-support at {total}@{sort}",
        supports_absence(verdict),
        rate >= 60.0 and sort == "updated",
    )

# ---------------------------------------------------------------- p238's re-attributed query
# Same query, same total_count, same day; the sort key is the only difference.
P238_Q = "FERPA OR COPPA student education in:name,description,readme license:mit pushed:>2026-06-01"
check("p238 query @updated is a slice", classify(10815, "updated", P238_Q)[0], "SLICE")
check("p238 query @stars is the head", classify(10815, "stars", P238_Q)[0], "HEAD")
check("p238 query @updated not harvestable", is_harvestable(classify(10815, "updated", P238_Q)[0]), False)
check("p238 query @stars harvestable for rows", is_harvestable(classify(10815, "stars", P238_Q)[0]), True)

# ---------------------------------------------------------------- threshold boundaries
check("at CAUTION_MAX still a sample", classify(CAUTION_MAX, "updated", "x")[0], "SAMPLE")
check("one above CAUTION_MAX narrows", classify(CAUTION_MAX + 1, "updated", "x")[0], "NARROW")
check("one below REFUSE_MIN narrows", classify(REFUSE_MIN - 1, "updated", "x")[0], "NARROW")
check("at REFUSE_MIN slices", classify(REFUSE_MIN, "updated", "x")[0], "SLICE")
check("NARROW is still harvestable", is_harvestable("NARROW"), True)
check("SLICE is not harvestable", is_harvestable("SLICE"), False)
check("HEAD IS harvestable for rows", is_harvestable("HEAD"), True)

# The three axes come apart, and the measurement is what separates them.
check("HEAD may not ground an absence", supports_absence("HEAD"), False)
check("HEAD may not ground recency", supports_recency("HEAD"), False)
check("NARROW may not ground an absence", supports_absence("NARROW"), False)
check("NARROW may ground recency", supports_recency("NARROW"), True)
check("SAMPLE grounds an absence", supports_absence("SAMPLE"), True)
check("SCOPED grounds an absence", supports_absence("SCOPED"), True)
check("SLICE grounds nothing", (is_harvestable("SLICE"), supports_absence("SLICE"), supports_recency("SLICE")), (False, False, False))

# p238's recorded absence, re-examined at both sort keys: neither shape could carry it,
# and p239 published 16 permissive North America rows by scoping the query instead.
check("p238 absence unsupported @stars", supports_absence(classify(10815, "stars", P238_Q)[0]), False)
check("p238 absence unsupported @updated", supports_absence(classify(10815, "updated", P238_Q)[0]), False)
check("scoped harvest could carry it", supports_absence(classify(24, "updated", "org:Ed-Fi-Alliance-OSS")[0]), True)

# ---------------------------------------------------------------- an absent sort key IS a recency sort
# The GitHub default is best-match, but 0 of 20 query-evidence files in this KB record a
# sort key at all, so an unrecorded sort cannot be assumed to have been a good one.
check("sort=None over a broad set is a slice", classify(50000, None, "broad")[0], "SLICE")
check("sort='' over a broad set is a slice", classify(50000, "", "broad")[0], "SLICE")
check("sort=None over a narrow set is fine", classify(100, None, "narrow")[0], "SAMPLE")

# ---------------------------------------------------------------- scoping beats sorting
for q in (
    "org:Ed-Fi-Alliance-OSS",
    "topic:education topic:ai-agent license:mit",
    "user:edanalytics dbt",
    "repo:Ed-Fi-Alliance-OSS/Fiona",
):
    check(f"has_scope({q[:22]})", has_scope(q), True)
    check(f"scoped at any breadth: {q[:22]}", classify(999999, "updated", q)[0], "SCOPED")

for q in ("Ed-Fi in:name,description", "FERPA OR COPPA student", "", "license:mit pushed:>2026-01-01"):
    check(f"not scoped: {q[:26]!r}", has_scope(q), False)

check("scope detection is case-insensitive", has_scope("ORG:Ed-Fi-Alliance-OSS"), True)

# ---------------------------------------------------------------- unrecorded / malformed input
check("missing total_count is a slice", classify(None, "stars", "x")[0], "SLICE")
check("negative total_count is a slice", classify(-1, "stars", "x")[0], "SLICE")
check("unknown sort key is a slice", classify(10, "relevance", "x")[0], "SLICE")
check("unknown sort key refused even when narrow", is_harvestable(classify(5, "popularity", "x")[0]), False)

# ---------------------------------------------------------------- relevance sort below the head
check("stars over a narrow set is a sample", classify(300, "stars", "x")[0], "SAMPLE")
check("forks over a narrow set is a sample", classify(300, "forks", "x")[0], "SAMPLE")
check("stars at REFUSE_MIN is still a sample", classify(REFUSE_MIN, "stars", "x")[0], "SAMPLE")
check("stars above REFUSE_MIN is the head", classify(REFUSE_MIN + 1, "stars", "x")[0], "HEAD")

# ---------------------------------------------------------------- every verdict carries a reason
for total, sort, query, _, _ in MEASURED:
    verdict, reason = classify(total, sort, query)
    check(f"reason given for {total}@{sort}", bool(reason and len(reason) > 20), True)

# A SLICE must say what to do instead, or it is a refusal without a remedy.
_, reason = classify(81905, "updated", "agente educativo")
check("slice reason names the remedy", ("org:" in reason or "stars" in reason), True)

if FAIL:
    print(f"FAIL {len(FAIL)}/{N}")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print(f"PASS {N}/{N}")
