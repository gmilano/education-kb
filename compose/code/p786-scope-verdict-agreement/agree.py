#!/usr/bin/env python3
"""p786 -- SCOPE-VERDICT agreement between the two licence instruments.

`p637` already cross-runs this KB's three *family classifiers* over ONE payload and its
lesson is written down: **it does not vote**, because the majority said `LGPL` and the
majority was wrong.  This instrument carries that lesson up one level, to the *verdict*:

    p784-licence-scope-map        16 ROOTED filenames -> SINGLE | PARTITIONED | UNGRANTED
    p441-tree-licence-enumeration complete `git ls-tree -r` -> OWN-GRANT-AT-ROOT | ...

Measured pass 62 over 13 slugs: 11 agree, 2 do not, and the two disagreements are opposite
in direction -- one refuses a usable repo, one admits an unlicensed one.

THE POINT THAT IS NOT OBVIOUS, and the reason this file exists rather than a tally:
`P786` -- a scope partition can be declared in PROSE and in no file either instrument
reads.  `luisgf/openbadgeslib` splits LGPL-3.0 library / BSD-2-Clause CLI in
`wiki/Authors-License-and-FAQ.md`; `LICENSE.txt` says LGPL-3.0 alone, `pyproject.toml`
carries one classifier, PyPI agrees, and 0 of 40 `.py` headers name BSD.  BOTH instruments
returned one family.  They AGREED, and they were BOTH WRONG.

So agreement is NOT a pass.  Every unanimous single-family verdict is emitted as
NEEDS-PROSE-READ, because that is the exact shape in which a prose-only partition hides.
This instrument narrows who a human must read, it never replaces them.

Usage:
    python3 agree.py --self-test
    python3 agree.py SLUGS_FILE          # one owner/repo per line
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))        # P355: never relative
P784 = os.path.join(HERE, "..", "p784-licence-scope-map", "probe.sh")
P441_DIR = os.path.join(HERE, "..", "p441-tree-licence-enumeration")

PERMISSIVE = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "BSD", "ISC"}

# p441 reports coarse families ("BSD", "LGPL?"); p784 reports SPDX-ish ones
# ("BSD-3-Clause", "LGPL-3.0").  A coarse value that PREFIXES a fine one is not a
# disagreement -- that is p637's CONTRATO class, and conflating it with a real
# divergence is how a tally turns into noise.
def comparable(a, b):
    a, b = a.rstrip("?"), b.rstrip("?")
    return a == b or a.startswith(b) or b.startswith(a)


def classify(p784_verdict, p784_families, p441_verdict, p441_families):
    """Return (class, note).  Never votes; never collapses a direction."""
    p784_families = [f for f in p784_families if f]
    p441_families = [f for f in p441_families if f]

    if p784_verdict == "UNREACHABLE" or p441_verdict == "UNREACHABLE":
        return "UNREACHABLE", "one or both channels did not resolve the slug"

    # Direction 1: p784 sustains an ABSENCE that p441's tree contradicts.  Gap 287.
    if p784_verdict == "UNGRANTED" and p441_families:
        return ("DISAGREE-ABSENCE",
                "p784 found no grant at 16 ROOTED names; the tree carries licence paths. "
                "Read `UNGRANTED` as UNGRANTED-AT-ROOT, never as unlicensed")

    # Direction 2: p441 claims families p784 never saw.  Gap 288 -- the regex matches
    # `licenseExtension`, so a schema doc about licences becomes a grant.  This
    # direction ADMITS, so it is reported even when p784 also found something.
    if p441_families and not any(
            any(comparable(x, y) for y in p784_families) for x in p441_families):
        return ("DISAGREE-PRESENCE",
                "p441 reports families p784 did not find; verify each path is a GRANT "
                "and not documentation ABOUT licences before relying on it")

    if p784_verdict == "PARTITIONED" or len(set(p784_families)) > 1:
        return "PARTITIONED-DECLARED", "scope split is visible in files; read scope per path"

    if p784_verdict == "UNGRANTED" and not p441_families:
        return ("ABSENCE-ENUMERATED",
                "no grant at 16 root names AND no licence path in the complete tree -- "
                "the only verdict a filename list could not reach on its own")

    # The unanimous case.  P786: this is where a prose-only partition hides.
    fam = p784_families[0] if p784_families else "?"
    return ("NEEDS-PROSE-READ",
            "both instruments agree on a single family (%s); read README and wiki/ before "
            "treating it as the whole grant (P786)" % fam)


def run_p784(slug):
    try:
        r = subprocess.run(["bash", P784, slug], capture_output=True, text=True, timeout=180)
    except (subprocess.TimeoutExpired, OSError):
        return "UNREACHABLE", []
    verdict, families = "UNREACHABLE", []
    for line in r.stdout.splitlines():
        if "VERDICT:" in line:
            tail = line.split("VERDICT:", 1)[1].strip()
            verdict = tail.split()[0]
            if "--" in tail:
                families = [tail.split("--", 1)[1].split("(")[0].strip()]
        elif line.startswith("   ") and len(line.split()) >= 3 and "VERDICT" not in line:
            parts = line.split()
            if len(parts) >= 2:
                families.append(parts[1])
    return verdict, [f for f in dict.fromkeys(families) if f and f != "VERDICT:"]


def run_p441(slugs):
    """One invocation for the whole batch -- p441 clones, so per-slug calls would refetch."""
    path = os.path.join(HERE, ".p786-slugs.tmp")
    with open(path, "w") as fh:
        fh.write("\n".join(slugs) + "\n")
    out = {}
    try:
        r = subprocess.run([sys.executable, "enumerate_licence.py", path],
                           capture_output=True, text=True, cwd=P441_DIR, timeout=1800)
        for line in r.stdout.splitlines()[1:]:
            col = line.split("\t")
            if len(col) >= 5:
                out[col[0]] = (col[1], [f for f in col[4].split(";") if f and f != "-"])
    except (subprocess.TimeoutExpired, OSError):
        pass
    finally:
        if os.path.exists(path):
            os.remove(path)
    return out


def main(argv):
    if not argv:
        sys.stderr.write(
            "p786: refusing to run with no arguments.\n"
            "  usage: python3 agree.py SLUGS_FILE   (or --self-test)\n"
            "  An instrument that reports success over an empty input is Gap 245's defect.\n")
        return 2
    if argv[0] == "--self-test":
        return 0 if _self_test() else 1
    try:
        slugs = [l.strip() for l in open(argv[0]) if l.strip() and not l.startswith("#")]
    except OSError as exc:
        sys.stderr.write("p786: cannot read %s: %s\n" % (argv[0], exc))
        return 2
    if not slugs:
        sys.stderr.write("p786: %s contains no slugs -- refusing (Gap 245)\n" % argv[0])
        return 2

    tree = run_p441(slugs)
    print("\t".join(["slug", "p784_verdict", "p784_families",
                     "p441_verdict", "p441_families", "class", "note"]))
    counts = {}
    for slug in slugs:
        v4, f4 = run_p784(slug)
        v1, f1 = tree.get(slug, ("UNREACHABLE", []))
        cls, note = classify(v4, f4, v1, f1)
        counts[cls] = counts.get(cls, 0) + 1
        print("\t".join([slug, v4, ";".join(f4) or "-", v1, ";".join(f1) or "-", cls, note]))
    print("#\ttotal\t%d\t%s" % (len(slugs),
                                " ".join("%s=%d" % kv for kv in sorted(counts.items()))))
    return 0


def _self_test():
    import unittest
    sys.argv = sys.argv[:1]
    loader = unittest.TestLoader()
    sys.path.insert(0, HERE)
    suite = loader.discover(HERE, pattern="test_agree.py")
    return unittest.TextTestRunner(verbosity=1).run(suite).wasSuccessful()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
