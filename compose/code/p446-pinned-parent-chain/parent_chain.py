#!/usr/bin/env python3
"""p446 - the depth-2 edge set has an unstated parameter: WHICH parent version.

P446: when a measurement walks a chain, every leg's version is a parameter.  A chain
with one leg unstated is not reproducible, and here that one leg moves the answer 3.4x.

`p442-depth2-pinned` answered pass 25's action B and published:

    depth-2 PINNED median = 334.5 d   against depth 1's 220 d
    -> "the ladder is monotone on both axes", trend 63

This instrument asks the same question with one leg changed, and gets 97 d.

## The two chains

Both resolve the depth-2 SPECIFIER to a pinned version the same way -- both import
`p437`'s resolver, so the second leg is identical.  They differ on WHOSE DEPENDENCY
LIST the specifier is read from:

    p442   depth-1 package's LATEST release   ->  info.requires_dist
                                                  versions[dist-tags.latest]
    p446   depth-1 package's PINNED version   ->  /pypi/<name>/<PINNED>/json
                                                  versions[<PINNED>]

A build installs the PINNED depth-1 package, so its dependency list is the pinned
one's.  `p437` resolved those pins already; reading `latest`'s list describes a tier
that is installed only where a pin happens to equal latest, which `p437` measured at
62%.  So for the question "how old is what a build installs two levels down", the
pinned-parent chain is the faithful one -- and `p442`'s number answers a different,
also-real question: "how old would the CURRENT depth-1 releases install".

## Why the pinned chain comes out YOUNGER, which is the counter-intuitive part

                          p442 (latest parent)    p446 (pinned parent)
    rows                  344 edges / 276 pkgs    891 edges / 410 pkgs
    median pinned age     334.5 d                 97 d
    EXACT share           21%                     11%
    EXACT median          49 d                    1,553 d
    CAPPED share          56%                     58%
    CAPPED median         694 d                   62 d

The two instruments disagree about WHICH CLASS carries the staleness, and both are
right about their own corpus.  With LATEST parents the CAPPED rows are current
libraries' wide ranges, which resolve to the newest release under a cap that may
itself be years old (694 d).  With PINNED parents the CAPPED rows mostly resolve to
current releases (62 d), because the cap is satisfied by today's version -- while the
EXACT rows become catastrophically old (1,553 d), because an old pinned parent
exact-pins whatever was current when it shipped.

So the headline reverses with the parameter.  `puppeteer-core` pinned at 13.5.0 (2022)
contributes 24 EXACT depth-2 rows, dragging in `rimraf 3.0.2` (+2,199 d behind its own
latest) and `https-proxy-agent 5.0.0` (+2,313 d); `puppeteer-core` at latest
contributes none of that.  Neither number is wrong.  Quoting either without naming the
parent version is.

Resolution and specifier classification are imported from `p437` -- rule 1 of P126 --
so the only new thing here is the FIRST LEG.

## Scope, inherited from p438/p442 so the three stay comparable

- Runtime dependencies only.  `extra == "..."` markers, npm `devDependencies`,
  `peerDependencies` and `optionalDependencies` are excluded.
- Markers other than `extra` are kept.
- Depth 2 means "required by a pinned depth-1 package", not the transitive closure.
- EDGES, not distinct packages.  891 rows cover 410 distinct names; a package reached
  from two parents is counted twice, because it is installed under two different
  constraints.  `p442` deduplicated to packages.  That is a second, smaller difference
  between the two instruments, and it is stated rather than reconciled away.

TSV: parent, parent_version, eco, dep, spec, spec_class, pinned_version,
     pinned_age, latest_version, latest_age, status
"""
import datetime as dt
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "p437-pinned-version"))
import pinned as P  # noqa: E402  -- resolve/releases/spec_class/get, one implementation


def runtime_deps(name, version, eco):
    """The runtime dependencies THIS EXACT version declares -> [(dep, spec)].

    Returns None when the version-specific endpoint does not answer, which is a
    different fact from "this version declares no dependencies" and must not be
    collapsed into an empty list -- P183's class.
    """
    out = []
    if eco == "pypi":
        c, t = P.get(f"https://pypi.org/pypi/{name}/{version}/json")
        if c != 200:
            return None
        for s in (json.loads(t)["info"].get("requires_dist") or []):
            # PEP 508: "name[extra] (>=1.0) ; marker".  An `extra == "..."`
            # marker makes the dependency optional -- `pip install <name>`
            # does not install it -- so it is out of scope, exactly as in p438.
            head, _, marker = s.partition(";")
            if re.search(r'\bextra\s*==', marker):
                continue
            m = re.match(r'\s*([A-Za-z0-9._-]+)\s*(?:\[[^\]]*\])?\s*(.*)', head)
            if not m:
                continue
            out.append((m.group(1), (m.group(2) or "").strip(" ()") or "*"))
        return out
    c, t = P.get(f"https://registry.npmjs.org/{name}")
    if c != 200:
        return None
    vs = (json.loads(t).get("versions") or {})
    if version not in vs:
        return None
    return [(d, s or "*") for d, s in (vs[version].get("dependencies") or {}).items()]


def main():
    ref = dt.date.fromisoformat(sys.argv[2])
    P.__dict__.setdefault("REF", ref)
    # Input: p437's resolved depth-1 rows -- the (name, pinned_version, eco)
    # triples a build actually installs.  Deduplicated by name+version, because
    # the same pinned package reached from two repos has one dependency list.
    parents, seen = [], set()
    with open(sys.argv[1]) as f:
        next(f)
        for line in f:
            c = line.rstrip("\n").split("\t")
            if len(c) < 11 or c[10] != "OK" or not c[6]:
                continue
            key = (c[2].lower(), c[6], c[3])
            if key in seen:
                continue
            seen.add(key)
            parents.append((c[2], c[6], c[3]))

    def one(p):
        name, ver, eco = p
        deps = runtime_deps(name, ver, eco)
        if deps is None:
            return [(name, ver, eco, "-", "-", "-", "", "", "", "", "PARENT-UNREADABLE")]
        if not deps:
            return [(name, ver, eco, "-", "-", "-", "", "", "", "", "NO-DEPS")]
        rows = []
        for dep, spec in deps:
            r = P.resolve(dep, spec, eco, ref)
            # r = (name, eco, spec, spec_class, pinned, pinned_age, latest, latest_age, status)
            rows.append((name, ver, eco, r[0], r[2], r[3], r[4], r[5], r[6], r[7], r[8]))
        return rows

    print("\t".join(["parent", "parent_version", "eco", "dep", "spec", "spec_class",
                     "pinned_version", "pinned_age", "latest_version", "latest_age",
                     "status"]))
    with ThreadPoolExecutor(max_workers=8) as ex:
        for rows in ex.map(one, parents):
            for r in rows:
                print("\t".join(str(x) for x in r))


if __name__ == "__main__":
    main()
