"""p150 — run the two-surface discriminator over every tree available, print a TSV."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gpl_affero as G  # noqa: E402

COLS = ["subject", "naive", "fixed", "status", "delta"]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    out = []
    for d in argv[1:]:
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            p = os.path.join(d, name)
            if os.path.isdir(p):
                out.append(G.census(p, name))
    print("\t".join(COLS))
    for r in sorted(out, key=lambda r: r["subject"]):
        print("\t".join(str(r[c]) for c in COLS))
    over = [r for r in out if r["delta"] == "OVERSTATED"]
    sys.stderr.write("trees=%d overstated=%d\n" % (len(out), len(over)))
    for r in over:
        sys.stderr.write("  OVERSTATED %-40s naive=%s fixed=%s\n"
                         % (r["subject"], r["naive"], r["fixed"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
