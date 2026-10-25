#!/usr/bin/env python3
"""p441 — the BSD population, graded.  ALWAYS EXITS 0: a MEASUREMENT target.

🔵 `Gap 435-A` and `Gap 438-B` both prescribe the same shape for a population question —
it belongs in a target that measures and never blocks a commit, with the controls that can
go red living in `test_grant_presence.py` against committed fixtures.  This file is that
target for `Gap 440-A`.

Two populations, reported apart because they answer different questions:

  FIXTURE  every BSD-titled payload under `compose/code/**/fixtures/**` — the population
           `Gap 440-A` enumerated as "BSD 14".  🔴 Three of those 14 are KB MARKDOWN
           TABLES that name a licence in a cell (`md-form4-italic.md`,
           `md-shortname-binding.md`, `md-page-said-header.md`), not licence payloads, so
           the real BSD payload count is 11 and the gap's denominator was 27 % high.
           `p310`'s rule: a family count is a claim about a corpus and needs its
           denominator attached.

  LIVE     every BSD row this base PUBLISHES, probed first-hand by
           `probe_bsd_shelves.sh` the same hour.  The family is taken from the hardened
           owner (`lib/license_family.sh`, via the probe) and PASSED IN, because four of
           the eleven carry no title line and `titled_family()` is title-only by
           construction.

Usage: grade_bsd.py [--root DIR] [--payloads DIR]
"""
import argparse
import collections
import glob
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "p439-grant-presence"))
sys.path.insert(0, str(HERE.parent / "p341-bespoke-instrument-census"))
import bespoke_census as bc  # noqa: E402
import grant_presence as gp  # noqa: E402

# The three fixtures that are KB prose rather than licence payloads.  Named, not inferred
# from a byte floor: each is a markdown table whose licence CELL is what `titled_family()`
# answered from.
NOT_A_PAYLOAD = ("md-form4-italic.md", "md-shortname-binding.md",
                 "md-page-said-header.md")


def fixture_rows(root):
    for p in sorted(glob.glob(str(root / "compose/code/**/fixtures/**"), recursive=True)):
        pp = pathlib.Path(p)
        if not pp.is_file():
            continue
        try:
            t = pp.read_text(errors="replace")
        except Exception:
            continue
        if len(t) < 40:
            continue
        if bc.grade(t)["titled_family"] != "BSD":
            continue
        r = gp.classify(t, "BSD")
        yield (pp.name, r["profile"] or "-", r["bytes"], r["verdict"],
               ",".join(r["missing"]) or "-",
               "prose" if pp.name in NOT_A_PAYLOAD else "payload")


def live_rows(payload_dir):
    for pp in sorted(pathlib.Path(payload_dir).glob("*.payload")):
        t = pp.read_text(errors="replace")
        titled = bc.grade(t)["titled_family"]
        r = gp.classify(t, "BSD")
        yield (pp.name.replace(".payload", ""), str(titled), r["profile"] or "-",
               r["bytes"], r["verdict"], ",".join(r["missing"]) or "-")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(HERE.parents[2]))
    ap.add_argument("--payloads", default=str(HERE / "payloads"))
    a = ap.parse_args(argv)

    print("population\tname\ttitled\tprofile\tbytes\tverdict\tmissing")
    fx = list(fixture_rows(pathlib.Path(a.root).resolve()))
    for name, prof, b, v, miss, kind in fx:
        print("FIXTURE-%s\t%s\tBSD\t%s\t%d\t%s\t%s" % (kind, name, prof, b, v, miss))
    live = list(live_rows(a.payloads)) if pathlib.Path(a.payloads).is_dir() else []
    for name, titled, prof, b, v, miss in live:
        print("LIVE\t%s\t%s\t%s\t%d\t%s\t%s" % (name, titled, prof, b, v, miss))

    print("#\tcifra\tvalue")
    print("#\tfixture_bsd_titled\t%d" % len(fx))
    print("#\tfixture_bsd_real_payloads\t%d" % len([r for r in fx if r[5] == "payload"]))
    print("#\tfixture_bsd_prose_not_payloads\t%d" % len([r for r in fx if r[5] == "prose"]))
    for k, c in sorted(collections.Counter(r[3] for r in fx).items()):
        print("#\tfixture_%s\t%d" % (k.lower().replace("-", "_"), c))
    print("#\tlive_rows_probed\t%d" % len(live))
    print("#\tlive_untitled_payloads\t%d" % len([r for r in live if r[1] == "None"]))
    for k, c in sorted(collections.Counter(r[4] for r in live).items()):
        print("#\tlive_%s\t%d" % (k.lower().replace("-", "_"), c))
    print("#\tGap 440-A: a MEASUREMENT, not a gate.  The controls are in "
          "p439-grant-presence/test_grant_presence.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
