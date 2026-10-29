"""Emit `evidence/liveness-fields.2026-10-29-p519.tsv` from ONE saved GitHub search payload.

🔵 Why one payload. `Gap 513-E` forbids a hard-coded count: every number `p519` publishes is
derived from the TSV this script writes, and the TSV is derived from a single API response read
`2026-10-29`, so a successor can re-derive both without trusting prose.

🔵 The licence column is an ASSERTION, not a copy. Each (slug, spdx) pair below was put to the
search API as `license:<spdx> repo:<slug> …` — a query that returns the repo ONLY if GitHub's own
classifier agrees. Two negative controls were included in those queries and both were correctly
refused, so the channel is known to discriminate rather than echo.

Usage:  python3 -I emit_evidence.py <saved-search-payload.json> <out.tsv>
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from liveness import classify, permissive, readable_grant, updated_at_is_not_liveness

TODAY = "2026-10-29"

# (slug -> (asserted spdx, assertion outcome)).  ASSERT_OK  = returned by the single-licence
# query, so GitHub's classifier agrees.  ASSERT_REFUSED = deliberately queried under a licence
# it does NOT carry and correctly not returned: a negative control.
ASSERTIONS = {
    "learningequality/kolibri":        ("MIT", "ASSERT_OK"),
    "academico-sis/academico":        ("MIT", "ASSERT_OK"),
    "jcputney/scorm-again":           ("MIT", "ASSERT_OK"),
    "karanb192/algo-sensei":          ("MIT", "ASSERT_OK"),
    "Li-Evan/Bloom":                  ("MIT", "ASSERT_OK"),
    "nichochar/ari":                  ("MIT", "ASSERT_OK"),
    "KeWang0622/kaogong-skill":       ("MIT", "ASSERT_OK"),
    "iblai/lms":                      ("MIT", "ASSERT_OK"),
    "SirhanMacx/Claw-ED":             ("MIT", "ASSERT_OK"),
    "beltromatti/get-it":             ("Apache-2.0", "ASSERT_OK"),
    "menthorlabs/menthor":            ("Apache-2.0", "ASSERT_OK"),
    "JuneYaooo/lineage-skill":        ("Apache-2.0", "ASSERT_OK"),
    "tsugiproject/tsugi":             ("Apache-2.0", "ASSERT_OK"),
    # negative control
    "chamilo/chamilo-lms":            ("MIT", "ASSERT_REFUSED"),
    # rows carried for the record, with NO licence assertion possible
    "canyongbs/advisingapp":          ("", "NO_ASSERTION_POSSIBLE"),
    "xiaoyang111222/cn-math-taxonomy": ("", "NO_ASSERTION_POSSIBLE"),
}

# 🔴 Region is recorded ONLY where the payload itself carries evidence (curriculum, language of
# the description, a named event).  `UNSTATED` and `UNRESOLVED-pt` are verdicts, not blanks:
# `Gap 513-C` is about rows that carry a GUESS, so nothing here is guessed.
REGION = {
    "Li-Evan/Bloom":                  ("APAC", "description is Chinese-first (中文优先 苏格拉底式 AI 家教)"),
    "KeWang0622/kaogong-skill":       ("APAC", "PRC civil-service exam (公务员/事业单位) scope"),
    "xiaoyang111222/cn-math-taxonomy": ("APAC", "aligned to the PRC national curriculum (课标)"),
    "beltromatti/get-it":             ("EMEA", "built at GDG AI Hack Milan 2026"),
    "menthorlabs/menthor":            ("UNRESOLVED-pt", "Portuguese description does not separate BR from PT"),
}


# 🔵 The SECOND negative control.  Each of the two single-licence queries carried one.  This pair
# cannot live in ASSERTIONS because `academico` legitimately holds its own ASSERT_OK row under
# MIT, and a slug may appear there once — so it is emitted as its own row instead of overwriting.
NEG_CONTROLS = [("academico-sis/academico", "Apache-2.0")]


def main():
    payload, out = sys.argv[1], sys.argv[2]
    items = json.load(open(payload)).get("items", [])
    by_slug = {r["full_name"]: r for r in items}

    rows = []
    for slug, (spdx, outcome) in sorted(ASSERTIONS.items()):
        r = by_slug.get(slug)
        if r is None:
            rows.append([slug, "ABSENT_FROM_PAYLOAD"] + [""] * 11)
            continue
        served = (r.get("license") or {}).get("spdx_id") or "NONE"
        archived = bool(r.get("archived"))
        pushed = (r.get("pushed_at") or "")[:10]
        updated = (r.get("updated_at") or "")[:10]
        grade = classify(archived, pushed, TODAY)
        lies = updated_at_is_not_liveness(archived, pushed, updated, TODAY)
        region, basis = REGION.get(slug, ("UNSTATED", "no evidence in payload"))
        rows.append([
            slug, served, spdx or "-", outcome,
            str(r.get("stargazers_count")), str(r.get("forks_count")),
            (r.get("created_at") or "")[:10], pushed, updated,
            r.get("default_branch"), "yes" if archived else "no",
            grade, "YES" if lies else "no", region, basis,
        ])

    for slug, spdx in NEG_CONTROLS:
        r = by_slug.get(slug)
        served = (r.get("license") or {}).get("spdx_id") or "NONE"
        rows.append([slug + " (neg-control)", served, spdx, "ASSERT_REFUSED",
                     str(r.get("stargazers_count")), str(r.get("forks_count")),
                     (r.get("created_at") or "")[:10], (r.get("pushed_at") or "")[:10],
                     (r.get("updated_at") or "")[:10], r.get("default_branch"),
                     "yes" if r.get("archived") else "no", "-", "-",
                     "-", "negative control, not a shelf row"])

    header = ["slug", "spdx_served", "spdx_asserted", "assertion", "stars", "forks",
              "created", "pushed", "updated", "default_branch", "archived",
              "liveness", "updated_at_would_lie", "region", "region_basis"]
    with open(out, "w") as fh:
        fh.write("\t".join(header) + "\n")
        for row in rows:
            fh.write("\t".join(row) + "\n")

    # ---- derived counts: the ONLY place p519's prose numbers may come from -------------
    graded = [r for r in rows if len(r) == 15]
    asserted = [r for r in graded if r[3] == "ASSERT_OK"]
    print("payload_items\t%d" % len(items))
    print("rows_written\t%d" % len(rows))
    print("assert_ok\t%d" % len(asserted))
    print("assert_refused_negative_controls\t%d"
          % len([r for r in graded if r[3] == "ASSERT_REFUSED"]))
    print("no_assertion_possible\t%d"
          % len([r for r in graded if r[3] == "NO_ASSERTION_POSSIBLE"]))
    print("served_agrees_with_assertion\t%d/%d"
          % (len([r for r in asserted if r[1] == r[2]]), len(asserted)))
    print("permissive_and_live\t%d"
          % len([r for r in asserted if permissive(r[1]) and r[11] == "LIVE"]))
    print("archived\t%d" % len([r for r in graded if r[10] == "yes"]))
    print("stale\t%d" % len([r for r in graded if r[11] == "STALE"]))
    print("updated_at_would_lie\t%d"
          % len([r for r in graded if r[12] == "YES"]))
    print("grant_unreadable\t%d"
          % len([r for r in graded if not readable_grant(r[1])]))
    print("region_unstated_or_unresolved\t%d/%d"
          % (len([r for r in graded if r[13].startswith(("UNSTATED", "UNRESOLVED"))]),
             len(graded)))


if __name__ == "__main__":
    main()
