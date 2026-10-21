#!/usr/bin/env python3
"""p370 — join the tree run, the licence payloads and the README domain check.

Input is what probe_tree.sh left on disk: the per-slug root-tree ENUMERATION, the
licence blobs it read at a pinned sha, and the README. Output is one row per slug:

  slug  status  head  refs  licence_path  bytes  family  domain  strong_terms  tree_n

🔵 Reproducible offline from the committed captures — the network is only in the probe.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, os.pardir, "p228-shelf-gate"))
sys.path.insert(0, os.path.join(HERE, os.pardir, "p370-domain-check"))
from classify_grant import classify            # noqa: E402  the base's own classifier
from domain_check import check as domain_check  # noqa: E402


def read(path, limit=None):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read(limit) if limit else fh.read()


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("adjudicate.py <tree-run.tsv> <trees-dir> — refusing (P541)\n")
        return 2
    run, outdir = argv[0], argv[1]
    print("\t".join(["slug", "status", "head", "refs", "licence_path", "bytes",
                     "family", "rung", "domain", "channel", "strong_terms", "tree_n"]))
    with open(run, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            if not line.strip():
                continue
            r = dict(zip(head, line.rstrip("\n").split("\t")))
            slug = r["slug"]
            key = slug.replace("/", "%")
            tree = read(os.path.join(outdir, key + ".tree")) or ""
            tree_n = len([l for l in tree.splitlines() if l.strip()
                          and l.strip() not in ("NO-REMOTE", "CLONE-FAILED")])
            readme = read(os.path.join(outdir, key + ".readme"), 20000)
            tree_names = [l.strip() for l in tree.splitlines() if l.strip()
                          and l.strip() not in ("NO-REMOTE", "CLONE-FAILED")]
            dom = domain_check(slug, readme, tree_names)

            cands = [p for p in (r.get("licence_paths") or "-").split(",") if p and p != "-"]
            if not cands:
                print("\t".join([slug, r["status"], r.get("head", "-"), r.get("refs", "0"),
                                 "-", "0", "NO-GRANT-IN-TREE", "-", dom["verdict"],
                                 dom["channel"], ";".join(dom["strong"][:6]) or "-",
                                 str(tree_n)]))
                continue
            for p in cands:
                body = read(os.path.join(outdir, "%s--%s.payload" % (key, p.replace("/", "%"))))
                if body is None:
                    fam, rung, nbytes = "UNREAD", "-", 0
                else:
                    nbytes = len(body.encode("utf-8", errors="replace"))
                    try:
                        # the base's classifier returns (family, where-it-was-read, note)
                        verdict = classify(body)
                        if isinstance(verdict, tuple):
                            fam = verdict[0] or "UNCLASSIFIED"
                            rung = (verdict[1] or "-") if len(verdict) > 1 else "-"
                        else:
                            fam, rung = (verdict or "UNCLASSIFIED"), "-"
                    except Exception as exc:          # a classifier defect is a finding
                        fam, rung = "CLASSIFIER-ERROR:%s" % type(exc).__name__, "-"
                print("\t".join([slug, r["status"], r.get("head", "-"), r.get("refs", "0"),
                                 p, str(nbytes), str(fam), str(rung), dom["verdict"],
                                 dom["channel"], ";".join(dom["strong"][:6]) or "-",
                                 str(tree_n)]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
