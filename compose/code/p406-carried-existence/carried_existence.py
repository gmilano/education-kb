#!/usr/bin/env python3
"""`p406-carried-existence` — `Gap 405-C`: the EXISTENCE of a CARRIED address, swept.

🔴 WHAT THIS CLOSES, AND WHY IT IS NOT A NEW CHANNEL.  `Gap 405-C` reads:

    no instrument re-checks a carried address's EXISTENCE.  Four addresses this base
    carries went unresolvable and only a pass that happened to clone them noticed
    ... this is the THIRD measurement of the same decay — `p332`'s 22 truncations and
    `p397`'s six non-existent carried slugs are the first two.

🟢 **The channel already existed and was already calibrated.**  `p293-slug-existence-oracle`
measured this proxy's refusal signature against a control pair and fixed the verdict
vocabulary, including the bound that makes the token `ABSENT-OR-PRIVATE` and not `ABSENT`.
🟢 **The POPULATION instrument already existed too**: `p351-address-shape` separates
*cannot be an address* from *may be an address*, and its own docstring hands this question
on by name — *"whether an address answers is `p293-slug-existence-oracle`'s question"*.

🔴 **So the gap was never a missing channel.  It was a missing SWEEP.**  `p293` judges
slugs a pass GUESSES (argv); `p400-candidate-membership` judges candidates a pass is about
to shelve.  Neither asks the question over the rows this base ALREADY CARRIES, and that is
the only population whose decay can make a published recommendation point at nothing.
This module is the composition, plus the three things a sweep needs that a one-off does
not: concurrency, a resumable cache, and a retry rule that refuses to read throttling as
absence.

    make gate-carried-existence          # offline controls, in `make hooks`
    carried_existence.py census          # the population, offline (no probe)
    carried_existence.py sweep --online --out evidence/... [--workers 12]

🔴 THE DEFECT THIS MODULE IS BUILT NOT TO COMMIT.  A sweep is concurrent, and github.com
answers a throttled probe with a transport error.  `p293`'s `CHANNEL_RE` already carries
`Too many concurrent`, so the verdict is correctly `CHANNEL-ERROR` — but a census that
divides unresolvable-by-total turns every throttled probe into **decay**, and the decay
rate then rises with the worker count.  🟢 **So `CHANNEL-ERROR` is excluded from BOTH
sides of the rate** (`decay_rate` below), each one is retried serially before it is
reported, and control `C12` asserts the exclusion by constructing the exact population
where including it would change the answer.  🔵 This is `p293`'s own bound one layer out:
*reading a transport failure as a statement about the slug* is the expensive error, and a
denominator is where a sweep commits it silently.

🟡 WHAT THIS DOES NOT CLAIM.  `ABSENT-OR-PRIVATE` is not `ABSENT` — a repository that
exists and went private answers identically, and nothing in this channel separates them
(`p293`'s `C9`, re-asserted here as `C9'` because a census is exactly where the token gets
rounded off).  A swept address is also not a LIVE RECOMMENDATION: this module reports
which shelf each unresolvable address sits on, and adjudicating a row is a pass's work,
not a gate's.  🔵 And `EXISTS-PUBLIC` says the address answers today, not that the
artefact is maintained — that is `p173-dormancy-bands`'s question.
"""
import argparse
import collections
import concurrent.futures
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, os.pardir, "p293-slug-existence-oracle"))
sys.path.insert(0, os.path.join(_HERE, os.pardir, "p351-address-shape"))
from slug_oracle import (VERDICTS, calibrate, classify, head_sha,  # noqa: E402
                         probe)
from address_shape import harvest, partition  # noqa: E402

# `p376`'s list, imported by value rather than re-chosen, so a shelf added there is swept here.
SHELF_FILES = [
    "agents/top.md", "agents/trending.md", "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md", "intel/market.md", "intel/trends.md", "intel/open-gaps.md",
    "compose/patterns.md",
]

# The verdicts that are a statement ABOUT THE SLUG.  `CHANNEL-ERROR` and `MALFORMED` are
# statements about the probe, and they belong on NEITHER side of a decay rate.
RESOLVED = frozenset({"EXISTS-PUBLIC", "EXISTS-NO-REFS"})
UNRESOLVED = frozenset({"ABSENT-OR-PRIVATE"})
INCONCLUSIVE = frozenset({"CHANNEL-ERROR", "MALFORMED"})


def repo_root(start=None):
    """Walk up to the directory holding the shelves.  `p355`'s cwd-portability rule."""
    d = os.path.abspath(start or _HERE)
    while True:
        if all(os.path.exists(os.path.join(d, p)) for p in SHELF_FILES[:3]):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            raise SystemExit("p406: no shelf root above %s" % (start or _HERE))
        d = parent


def shelf_paths(root):
    return [os.path.join(root, p) for p in SHELF_FILES]


def population(root):
    """folded address -> sorted shelves naming it.  p351 decides what IS an address."""
    paths = shelf_paths(root)
    idx = harvest(paths)
    addresses, _rejected = partition(idx)
    where = collections.defaultdict(set)
    for rel, full in zip(SHELF_FILES, paths):
        with open(full, encoding="utf-8") as fh:
            body = fh.read().lower()
        for a in addresses:
            if a in body:
                where[a].add(rel)
    return {a: sorted(where[a]) for a in sorted(addresses)}


def decay_rate(verdicts):
    """(resolved, unresolved, inconclusive, rate) — rate over the GRADED half only.

    🔴 `inconclusive` is excluded from the numerator AND the denominator.  A sweep that
    counted it as unresolvable would publish a decay rate that climbs with its own worker
    count; one that counted it as resolved would publish a base healthier than it is.
    """
    c = collections.Counter(verdicts)
    res = sum(c[v] for v in RESOLVED)
    unres = sum(c[v] for v in UNRESOLVED)
    inc = sum(c[v] for v in INCONCLUSIVE)
    graded = res + unres
    return (res, unres, inc, (100.0 * unres / graded) if graded else None)


def load_cache(path):
    if not path or not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_cache(path, cache):
    if not path:
        return
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(cache, fh, indent=0, sort_keys=True)
    os.replace(tmp, path)


def sweep(addresses, workers=12, timeout=30, cache=None, retry=True, probe_fn=None,
          progress=None):
    """address -> (verdict, sha, detail).  ONLINE unless `probe_fn` is injected.

    Retries every INCONCLUSIVE row serially once.  Throttling is the expected cause under
    concurrency, and a serial retry is the cheapest discriminator between "the channel was
    busy" and "the channel answers this way for this slug".
    """
    pfn = probe_fn or (lambda url: probe(url, timeout))
    cache = cache if cache is not None else {}
    todo = [a for a in addresses if a not in cache]
    out = dict(cache)

    def one(a):
        text, rc = pfn("https://github.com/" + a)
        verdict, detail = classify(text, rc)
        return a, (verdict, head_sha(text) or "-", detail)

    if todo:
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
            for i, (a, row) in enumerate(ex.map(one, todo), 1):
                out[a] = row
                if progress and i % progress == 0:
                    sys.stderr.write("p406: %d/%d probed\n" % (i, len(todo)))
                    sys.stderr.flush()

    if retry:
        again = [a for a in addresses if out.get(a, ("MALFORMED",))[0] in INCONCLUSIVE]
        for a in again:
            verdict, sha, detail = out[a]
            text, rc = pfn("https://github.com/" + a)
            v2, d2 = classify(text, rc)
            out[a] = (v2, head_sha(text) or "-", d2 + " [serial retry after %s]" % verdict)
    return out


def head_collisions(rows):
    """sha -> [addresses].  Two names at one HEAD is p283's finding, not a verdict."""
    by = collections.defaultdict(list)
    for a, (verdict, sha, _d) in rows.items():
        if verdict == "EXISTS-PUBLIC" and sha and sha != "-":
            by[sha].append(a)
    return {s: sorted(v) for s, v in by.items() if len(v) > 1}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("mode", choices=("census", "sweep"))
    ap.add_argument("--online", action="store_true")
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--timeout", type=int, default=30)
    ap.add_argument("--cache")
    ap.add_argument("--out")
    ap.add_argument("--limit", type=int, help="probe only the first N (for a smoke run)")
    args = ap.parse_args(argv)

    root = repo_root()
    pop = population(root)
    if not pop:
        sys.stderr.write("p406: the shelves name no address — refusing to publish a rate\n")
        return 2

    if args.mode == "census":
        print("cifra\tvalor")
        print("shelves\t%d" % len(SHELF_FILES))
        print("addresses_carried\t%d" % len(pop))
        byshelf = collections.Counter()
        for _a, shelves in pop.items():
            for s in shelves:
                byshelf[s] += 1
        for s in SHELF_FILES:
            print("shelf:%s\t%d" % (s, byshelf[s]))
        print("# offline: no probe was made.  `sweep --online` asks whether they answer.")
        return 0

    if not args.online:
        print("offline: population is %d addresses over %d shelves." % (len(pop), len(SHELF_FILES)))
        print("verdict vocabulary: " + " ".join(VERDICTS))
        print("graded half = %s ; excluded from the rate = %s"
              % ("|".join(sorted(RESOLVED | UNRESOLVED)), "|".join(sorted(INCONCLUSIVE))))
        print("run `sweep --online` to probe; p293's control pair gates every verdict.")
        return 0

    ok, rows = calibrate(args.timeout)
    for leg, url, verdict, detail in rows:
        print("%-14s %-56s %-18s %s" % (leg, url, verdict, detail))
    if not ok:
        print("\n🔴 CALIBRATION FAILED — no verdict is reported (p293's gate, inherited).")
        return 1
    print("\n🟢 calibrated.\n")

    addresses = sorted(pop)
    if args.limit:
        addresses = addresses[:args.limit]
    cache = load_cache(args.cache)
    results = sweep(addresses, workers=args.workers, timeout=args.timeout,
                    cache={a: tuple(v) for a, v in cache.items() if a in addresses},
                    progress=200)
    save_cache(args.cache, {a: list(v) for a, v in results.items()})

    verdicts = [results[a][0] for a in addresses]
    res, unres, inc, rate = decay_rate(verdicts)
    counts = collections.Counter(verdicts)
    print("cifra\tvalor")
    print("addresses_probed\t%d" % len(addresses))
    for v in VERDICTS:
        print("%s\t%d" % (v, counts[v]))
    print("graded\t%d" % (res + unres))
    print("inconclusive_excluded\t%d" % inc)
    print("decay_rate\t%s" % ("%.2f%%" % rate if rate is not None else "UNDEFINED"))

    coll = head_collisions(results)
    for sha, slugs in sorted(coll.items()):
        print("# HEAD-COLLISION %s\t%s" % (sha[:12], ", ".join(slugs)))

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write("# p406-carried-existence — every address these shelves CARRY, probed.\n")
            fh.write("# Channel and vocabulary are p293's; population is p351's.\n")
            fh.write("# ABSENT-OR-PRIVATE does NOT mean absent: a private repository answers\n")
            fh.write("# identically and this channel cannot separate them (p293 C9).\n")
            fh.write("# CHANNEL-ERROR/MALFORMED are excluded from both sides of decay_rate.\n")
            fh.write("address\tverdict\thead_sha\tshelves\tdetail\n")
            for a in addresses:
                v, sha, detail = results[a]
                fh.write("%s\t%s\t%s\t%s\t%s\n"
                         % (a, v, sha, ";".join(pop[a]), detail.replace("\t", " ")))
        print("\nwrote %s" % args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
