#!/usr/bin/env python3
"""`p349-name-collision` — `ACTION ZZ-ag`'s shelf-wide HEAD-equality run, made AFFORDABLE.

p348 left ZZ-ag asking for the HEAD-equality test over all **2 462 folded addresses** on
the nine published shelves, after proving that the run p347 called shelf-wide had covered
17.4 % of them.  Run literally that is 2 462 network probes, which no pass has an hour
for -- so ZZ-ag has been, in practice, unrunnable rather than unrun.

🔵 **This instrument is the observation that makes it runnable: every alias pair this base
has ever found shares its REPOSITORY NAME.**

    digitalcredentials/learner-credential-wallet   ==  openwallet-foundation-labs/learner-credential-wallet
    microsoft/presidio                             ==  data-privacy-stack/presidio

An org transfer moves the owner and keeps the name, because the name is what the
project is called.  So the ONLINE probe only has to visit the addresses whose folded
repository NAME is shared by two or more distinct folded OWNERS -- a set this script
computes with no network at all.

🔴 **The declared blind spot, stated before the yield so it cannot be read as a result:**
a transfer that ALSO RENAMES the repository is invisible to this pre-filter, exactly as
the case fold is invisible to a renamed owner.  The pre-filter is a COST REDUCTION with a
known hole, never a proof of absence; a pass that reports "no further aliases" on this
channel alone has overclaimed.  Closing that hole needs the full 2 462-probe run or a
payload digest (`ACTION ZZ-ad`), and this file's verdict column says which question it
answered.

    name_collision.py probe   <shelf files...>  -> the bounded probe list, TSV
    name_collision.py census  <shelf files...>  -> denominators only
"""
import collections
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                os.pardir, "p348-fold-identity"))
from fold_identity import slugs_in  # noqa: E402  the harvester is p348's, not rewritten


def harvest(paths):
    """folded slug -> {as published}, over whole files (history included)."""
    idx = collections.defaultdict(set)
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            for s in slugs_in(fh.read()):
                idx[s.lower()].add(s)
    return idx


def name_groups(idx):
    """folded repo name -> sorted folded addresses, for names with >1 distinct owner."""
    byname = collections.defaultdict(set)
    for folded in idx:
        owner, _, name = folded.partition("/")
        byname[name].add(folded)
    out = {}
    for name, addrs in byname.items():
        owners = {a.partition("/")[0] for a in addrs}
        if len(owners) > 1:
            out[name] = sorted(addrs)
    return out


def main(argv):
    mode = "probe"
    if argv and argv[0] in ("probe", "census"):
        mode, argv = argv[0], argv[1:]
    # P541: a measurement over the files it is GIVEN must refuse an empty argument list.
    if not argv:
        sys.stderr.write("p349-name-collision: no shelf files given — refusing "
                         "(P541: `total 0` with no input is not a clean tree)\n")
        return 2
    idx = harvest(argv)
    groups = name_groups(idx)
    probes = sum(len(v) for v in groups.values())
    if mode == "census":
        print("folded_addresses\t%d" % len(idx))
        print("collision_names\t%d" % len(groups))
        print("bounded_probes\t%d" % probes)
        print("reduction\t%.1f%%" % (100.0 * (1 - probes / float(len(idx) or 1))))
        return 0
    print("name\taddress")
    for name in sorted(groups):
        for a in groups[name]:
            print("%s\t%s" % (name, a))
    sys.stderr.write("# %d folded addresses -> %d collision names -> %d probes (%.1f%% fewer)\n"
                     % (len(idx), len(groups), probes,
                        100.0 * (1 - probes / float(len(idx) or 1))))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
