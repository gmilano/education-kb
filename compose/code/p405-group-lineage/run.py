"""Read forkgroup.sh's facts cache, grade every pair, print two TSVs.

Separated from the collector so the grading is exercised by `test_group_lineage.py`
without network, and so a committed cache can be re-graded without re-cloning.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grouplineage import Address, grade_group  # noqa: E402

PAIR_HEADER = ("group", "addr_a", "addr_b", "commits_a", "commits_b", "shared_commits",
               "shared_trees", "a_contains_b_head", "b_contains_a_head", "verdict",
               "direction")
ADDR_HEADER = ("group", "address", "status", "head12", "branch", "head_date", "refs_clonelocal",
               "tags", "commits", "trees", "roots", "root12", "root_date", "root_author",
               "licence_path", "licence_bytes", "licence_title", "component")


def read_facts(path):
    """A facts file -> {key: [values]}.  Multi-valued keys keep every value."""
    out = {}
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if "\t" not in line:
                continue
            k, v = line.rstrip("\n").split("\t", 1)
            out.setdefault(k, []).append(v)
    return out


def one(facts, key, default="-"):
    return facts.get(key, [default])[0]


def main(argv):
    group, cache, slugs = argv[1], argv[2], argv[3:]
    facts = {s: read_facts(os.path.join(cache, s.replace("/", "_"))) for s in slugs}
    resolved, unresolved = [], []
    for s in slugs:
        f = facts[s]
        if one(f, "status") != "OK":
            unresolved.append(s)
            continue
        resolved.append(Address(s, f.get("commit", []), f.get("tree", []),
                                one(f, "head"), f.get("root", []),
                                f.get("root_tree", []), f.get("ancestor", [])))
    rows, comps, summary = grade_group(resolved)

    where = {}
    for i, comp in enumerate(comps, 1):
        label = "SOLE" if len(comp) == 1 else "FAMILY-%d(n=%d)" % (i, len(comp))
        for s in comp:
            where[s] = label

    print("\t".join(ADDR_HEADER))
    for s in slugs:
        f = facts[s]
        if one(f, "status") != "OK":
            print("\t".join([group, s, "UNRESOLVED"] + ["-"] * (len(ADDR_HEADER) - 3)))
            continue
        a = next(x for x in resolved if x.slug == s)
        print("\t".join(str(x) for x in (
            group, s, "OK", a.head[:12], one(f, "branch"), one(f, "head_date"),
            one(f, "refs"), one(f, "tags"), len(a.commits), len(a.trees),
            len(a.roots), sorted(a.roots)[0][:12] if a.roots else "-",
            one(f, "root_date"), one(f, "root_author"), one(f, "licence_path", "NONE"),
            one(f, "licence_bytes", "-"), one(f, "licence_title", "-"), where[s])))

    print()
    print("\t".join(PAIR_HEADER))
    for r in rows:
        print("\t".join([group] + [str(x) for x in r]))

    print()
    print("# group=%s addresses=%d resolved=%d unresolved=%d pairs=%d"
          % (group, len(slugs), len(resolved), len(unresolved), len(rows)))
    print("# verdicts " + " ".join("%s=%d" % kv for kv in sorted(summary.items())))
    print("# families " + " ".join("[%s]" % ",".join(c) for c in comps if len(c) > 1)
          + (" none" if all(len(c) == 1 for c in comps) else ""))
    if unresolved:
        print("# unresolved " + " ".join(unresolved))


if __name__ == "__main__":
    main(sys.argv)
