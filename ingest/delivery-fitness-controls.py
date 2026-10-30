#!/usr/bin/env python3
"""delivery-fitness-controls.py -- negative controls for delivery-fitness.py (p556).

The live education harvest exercises three of the five verdict arms: on
`evidence/platform-harvest.2026-10-30-p556.tsv` the counts are BUILD-ON 25,
SELF-HOST-ONLY 11, BLOCK 6 over 42 rows, and LINK-ONLY and ASK are both ZERO.  An arm that no
row reaches is an arm that ships unrun, so the fixture asserts all five, and the
expected verdict is written beside each licence in the fixture file itself.

    python3 -I ingest/delivery-fitness-controls.py
    python3 -I ingest/delivery-fitness-controls.py evidence/OTHER-fixture.tsv

Exits 1 on any mismatch, or if any of the five arms is unexercised -- a fixture
that stops covering an arm is itself a defect.
"""
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT = ROOT / "evidence" / "delivery-fitness-fixture.p556.tsv"
ARMS = {"BUILD-ON", "LINK-ONLY", "SELF-HOST-ONLY", "BLOCK", "ASK"}


def load_module():
    spec = importlib.util.spec_from_file_location("df", HERE / "delivery-fitness.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(argv):
    path = pathlib.Path(argv[1]) if len(argv) > 1 else DEFAULT
    df = load_module()
    rows = df.read_harvest(path)
    bad, seen = 0, {}
    for r in rows:
        got, _ = df.grade(r["spdx_id"])
        seen[got] = seen.get(got, 0) + 1
        if got != r.get("expect"):
            print(f"FAIL {r.get('slug')}: spdx={r['spdx_id']} "
                  f"expect={r.get('expect')} got={got}")
            bad += 1
    print(f"fixture {path}: {len(rows)} row(s), {bad} mismatch(es)")
    for arm in sorted(ARMS):
        print(f"  arm {arm:<15} {seen.get(arm, 0)}")
    missing = sorted(ARMS - set(seen))
    if missing:
        print(f"FAIL: arm(s) unexercised by this fixture: {', '.join(missing)}")
        return 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
