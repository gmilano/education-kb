#!/usr/bin/env python3
"""p397 — discharge `396-F`'s ranked-first ask at SHELF SCALE.

`396-F` built a root-commit fork arm and stated its limit: "It needs a suspected
upstream to compare against — discovery of the pair is still WebSearch's job."
That is what kept it to new addresses only.

This derives the pairs from the shelves instead, with NO network: two shelf
addresses that share a repository NAME under different OWNERS are a fork
candidate. The root-commit arm then adjudicates only those pairs.
"""
import sys, os, collections
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "p351-address-shape"))
import address_shape

def main(argv):
    idx = address_shape.harvest(argv)
    # p351 owns the rejection classes; this instrument must NOT re-implement them,
    # or its denominator silently diverges from the published census.
    addrs, rejected = address_shape.partition(idx)
    by_name = collections.defaultdict(set)
    for a in addrs:
        owner, _, name = a.partition("/")
        if owner and name:
            by_name[name].add(owner)
    groups = {n: sorted(o) for n, o in by_name.items() if len(o) > 1}
    pairs = sum(len(o) * (len(o) - 1) // 2 for o in groups.values())
    print("cifra\tvalor")
    print(f"harvested_folded\t{len(idx)}")
    print(f"rejected_non_addresses\t{len(rejected)}")
    print(f"shelf_addresses\t{len(addrs)}")
    print(f"distinct_repo_names\t{len(by_name)}")
    print(f"name_collision_groups\t{len(groups)}")
    print(f"candidate_pairs\t{pairs}")
    print()
    print("name\towners")
    for n in sorted(groups):
        print(f"{n}\t{' '.join(groups[n])}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
