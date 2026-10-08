#!/usr/bin/env python3
"""P791 — a registry's REACHABILITY and a package's EXISTENCE are read off different probes.

`P793` is the same cut on the OTHER axis: a ref name is not provenance either. See
`ref_provenance()`.

`P787` partitioned reachability by HOST. This module partitions it once more, and the cut is
underneath P787's: even on ONE host, the code a target id returns is not a reachability
measurement. It is a fact about THAT ID. Two passes of this shelf read it as the host:

    pass 61  `packagist` **404**                       -> written into the oracle map
    pass 62  `packagist` **200 — recovered from 404**   -> written into the oracle map

Both probed `packbackbooks/lti-1-3-php-library` — the REPOSITORY slug, shaped like a package id.
Nothing publishes that id. `monolog/monolog` answers 200 and an invented id answers 404 on the
same host in the same minute, so the host never moved.

The gate, and it is the whole module:

  * a HOST verdict may be read ONLY from a calibration pair (one id known to exist, one known
    not to). `host_verdict()` will not accept a target's code at all.
  * a package verdict on a GUESSED id is `UNDETERMINED`, which is `p253`'s COMPUERTA 1 — reused,
    not reimplemented. This module imports `identity.py` and does not copy a line of it.

`P713`: re-measure the DATUM every pass; REUSE the instrument.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "p253-registry-first-identity"))
from identity import load, package_identity  # noqa: E402  (the instrument, unchanged)

#: codes that mean "the channel answered"; `000` is no answer at all
ANSWERED = {"200", "404"}


def host_verdict(good_code, bad_code):
    """The ONLY admissible source of a host line in the oracle map: a calibration pair.

    Deliberately takes no target id. A caller that wants to say "packagist is down" has to
    produce a pair, and the pair is what pass 61 and pass 62 never produced.
    """
    g, b = str(good_code), str(bad_code)
    if g == "200" and b == "404":
        return ("REACHABLE-DISCRIMINATING", "200 to a known id, 404 to an invented one")
    if g not in ANSWERED and b not in ANSWERED:
        return ("UNREACHABLE", f"no answer either way (good={g} bad={b})")
    if g == "200" and b == "200":
        return ("REACHABLE-NOT-DISCRIMINATING", "a 404 from this host would not be evidence")
    return ("INDETERMINATE", f"the pair does not settle it (good={g} bad={b})")


def id_provenance(row):
    """Did the SLUG-SHAPED guess and the TREE-DECLARED id give the same answer?

    When they disagree, a pass that probed only the guess wrote down the wrong fact — and the
    direction of the error is the point: `404` on the guess with `200` on the declared id is a
    FALSE ABSENCE, which `P788` already named the worse direction.
    """
    declared, guessed = str(row.get("tree_name_http", "-")), str(row.get("guessed_http", "-"))
    tree = row.get("tree_name")
    if tree in (None, "", "-"):
        return ("NO-DECLARATION", "no composer.json read: the guess is the only id there is")
    if row.get("tree_name") == row.get("slug"):
        return ("ID-EQUALS-SLUG", "guess and declaration coincide: no misread possible here")
    if declared == "200" and guessed != "200":
        return ("FALSE-ABSENCE-RISK",
                f"declared {tree} -> {declared}, slug-shaped guess -> {guessed}: "
                "probing the guess reports the package, and the host, as absent")
    if declared != "200" and guessed == "200":
        return ("FALSE-PRESENCE-RISK",
                f"declared {tree} -> {declared}, slug-shaped guess -> {guessed}: "
                "the guess lands on a package this repository does not declare")
    return ("AGREES", f"both ids -> declared {declared} / guess {guessed}")


def ref_provenance(row):
    """`P793` — `master` is a PSEUDO-REF on `raw.githubusercontent.com`.

    Measured this pass, 3 of 3, against a 404-discriminating control: `raw` serves the DEFAULT
    branch for the literal ref `master` even when the repository has no `master`, while `main`
    404s and an invented name 404s. So a row whose provenance reads "`master`" may have been
    read at `refs/heads/0.7`, `refs/heads/public` or `refs/heads/2.12`.

    The only ref oracle reachable from this host is `git ls-remote --symref … HEAD` (`P732`).
    This verdict compares what the oracle says to what actually served the bytes.
    """
    dref = str(row.get("default_ref", "-"))
    served = str(row.get("served_at", "-"))
    if served == "-":
        return ("NO-MANIFEST-FOUND", "no composer.json at the default ref or at either pseudo-ref")
    if dref == "-":
        return ("REF-ORACLE-SILENT", f"served at {served} with no ls-remote default: not provenance")
    if served == dref and dref not in ("main", "master"):
        return ("DEFAULT-IS-NEITHER",
                f"default ref is `{dref}`: a sweep reading only main/master cites a pseudo-ref")
    if served == dref:
        return ("DEFAULT-IS-NAMED", f"the default ref really is `{dref}`")
    return ("SERVED-OFF-DEFAULT", f"bytes came from `{served}`, default is `{dref}`")


def rows_with(path):
    """Every row with all three verdicts, `p253`'s among them."""
    out = []
    for r in load(path):
        out.append((r, package_identity(r), id_provenance(r), ref_provenance(r)))
    return out


def _main(path):
    seen = {}
    print("\t".join(["slug", "default_ref", "head_sha", "served_at", "tree_name",
                     "declared_license", "declared_http", "guessed_http", "p253_verdict",
                     "p791_provenance", "p793_ref", "latest", "latest_time"]))
    for r, p253, prov, br in rows_with(path):
        seen[prov[0]] = seen.get(prov[0], 0) + 1
        print("\t".join([r.get("slug", "-"), r.get("default_ref", "-"),
                         r.get("head_sha", "-"), r.get("served_at", "-"),
                         r.get("tree_name", "-"), r.get("declared_license", "-"),
                         r.get("tree_name_http", "-"), r.get("guessed_http", "-"),
                         p253[0], prov[0], br[0],
                         r.get("latest", "-"), r.get("latest_time", "-")]))
    print("\n# provenance census", file=sys.stderr)
    for k in sorted(seen, key=lambda x: -seen[x]):
        print(f"#   {k}\t{seen[k]}", file=sys.stderr)


if __name__ == "__main__":
    _main(sys.argv[1] if len(sys.argv) > 1 else "result.2026-10-08.tsv")
