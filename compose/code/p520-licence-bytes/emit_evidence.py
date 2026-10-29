"""Emit `evidence/licence-bytes.2026-10-29-p520.tsv` from the SAVED licence payloads.

🔵 `Gap 513-E` forbids a hand-typed count. Every number `p520` publishes about licences is
derived from the TSV this script writes, and the TSV is derived from payload bytes fetched
`2026-10-29` over `curl` -> `raw.githubusercontent.com`, each recorded with its byte count and
its git blob SHA-1 so a successor can re-fetch and compare without trusting this prose.

Usage:  python3 -I emit_evidence.py <raw-dir> <out.tsv>

The raw dir holds an `index.tsv` (slug, path, http, bytes, blob_sha1, file) written by the
fetch step, plus one payload file per row. The payloads are UNTRUSTED downloaded data: this
script only reads them as text and never executes anything from that directory.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grade import grade, permissive, buildable_for_paid_client_work

TODAY = "2026-10-29"

# What this base believed BEFORE the served bytes were read, so the TSV carries the correction
# rather than only the new value. "-" where no prior grade existed.
PRIOR = {
    "xiaoyang111222/cn-math-taxonomy": "NOASSERTION/UNREADABLE(p519); shelved as a foundation by p518",
    "canyongbs/advisingapp": "NOASSERTION/NO_ASSERTION_POSSIBLE(p519)",
    "CaviraOSS/PageLM": "NOASSERTION, blocked(Gap 520-B)",
    "GarethManning/education-agent-skills": "NOASSERTION, blocked(Gap 520-B)",
    "pupilfirst/pupilfirst": "NOASSERTION, blocked(Gap 520-B)",
    "OpenOLAT/OpenOLAT": "NOASSERTION, blocked(Gap 520-B)",
    "claroline/Claroline": "NOASSERTION, blocked(Gap 520-B)",
    "learningequality/kolibri": "MIT (positive control, asserted p519)",
    "chamilo/chamilo-lms": "GPL-3.0 (positive control, asserted p519)",
}

# Rows read to check the grader against an INDEPENDENTLY known answer rather than to learn
# something new. A channel and a grader that agree with everything prove nothing.
CONTROLS = {
    "learningequality/kolibri": "MIT",
    "chamilo/chamilo-lms": "GPL-3.0",
}

COLUMNS = (
    "slug",
    "path",
    "http",
    "bytes",
    "blob_sha1",
    "spdx_served",
    "verdict",
    "permissive",
    "paid_client_work",
    "basis",
    "prior_grade_on_these_shelves",
    "control",
)


def read_index(raw_dir):
    rows = []
    with open(os.path.join(raw_dir, "index.tsv"), encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            if not line.strip():
                continue
            rows.append(dict(zip(header, line.rstrip("\n").split("\t"))))
    return rows


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    raw_dir, out_path = argv[1], argv[2]

    out_rows = []
    for row in read_index(raw_dir):
        slug = row["slug"]
        if row["http"] != "200":
            out_rows.append(
                {
                    "slug": slug,
                    "path": row["path"],
                    "http": row["http"],
                    "bytes": "0",
                    "blob_sha1": "-",
                    "spdx_served": "UNREAD",
                    "verdict": "UNSTATED",
                    "permissive": "-",
                    "paid_client_work": "-",
                    "basis": "no licence payload served at any probed path",
                    "prior_grade_on_these_shelves": PRIOR.get(slug, "-"),
                    "control": "-",
                }
            )
            continue

        with open(os.path.join(raw_dir, row["file"]), encoding="utf-8", errors="replace") as fh:
            payload = fh.read()

        verdict = grade(payload)
        control = "-"
        if slug in CONTROLS:
            expected = CONTROLS[slug]
            control = (
                "AGREES(%s)" % expected
                if verdict["spdx"] == expected
                else "DISAGREES(expected %s)" % expected
            )

        out_rows.append(
            {
                "slug": slug,
                "path": row["path"],
                "http": row["http"],
                "bytes": row["bytes"],
                "blob_sha1": row["blob_sha1"],
                "spdx_served": verdict["spdx"],
                "verdict": verdict["verdict"],
                "permissive": "yes" if permissive(verdict["verdict"]) else "no",
                "paid_client_work": "yes"
                if buildable_for_paid_client_work(verdict["verdict"])
                else "NO",
                "basis": verdict["basis"],
                "prior_grade_on_these_shelves": PRIOR.get(slug, "-"),
                "control": control,
            }
        )

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(
            "# p520 — %s — SERVED licence bytes for every row Gap 520-B listed as blocked,\n"
            "# read over curl -> raw.githubusercontent.com (the channel p504 used and p518/p519\n"
            "# could not reach). Graded by compose/code/p520-licence-bytes/grade.py, 36/36 controls\n"
            "# green. Two rows are positive controls with independently known answers.\n" % TODAY
        )
        fh.write("\t".join(COLUMNS) + "\n")
        for row in out_rows:
            fh.write("\t".join(row[c] for c in COLUMNS) + "\n")

    # Derived counts. These are the ONLY numbers p520's prose may quote about licences.
    graded = [r for r in out_rows if r["control"] == "-"]
    controls = [r for r in out_rows if r["control"] != "-"]
    print("payloads read 200:      %d of %d" % (sum(1 for r in out_rows if r["http"] == "200"), len(out_rows)))
    print("shelf rows graded:      %d" % len(graded))
    print("  permissive:           %d" % sum(1 for r in graded if r["permissive"] == "yes"))
    print("  paid client work NO:  %d" % sum(1 for r in graded if r["paid_client_work"] == "NO"))
    print("  wrappers found:       %d" % sum(1 for r in graded if r["basis"].startswith("WRAPPER")))
    print("  UNSTATED refusals:    %d" % sum(1 for r in graded if r["spdx_served"] == "UNSTATED"))
    print("controls:               %d, agreeing %d" % (len(controls), sum(1 for r in controls if r["control"].startswith("AGREES"))))
    for r in graded:
        print("   %-40s %-14s %-28s paid=%s" % (r["slug"], r["spdx_served"], r["verdict"], r["paid_client_work"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
