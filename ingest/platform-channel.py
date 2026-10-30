#!/usr/bin/env python3 -I
"""p555 -- THE PLATFORM CHANNEL, JOINED TO THE THREE `doc-channel.py` ALREADY READS.

WHY THIS EXISTS, AND WHAT IT CORRECTS
-------------------------------------
`Gap 554-A` recorded the platform field as UNREACHABLE and bounded four claims on
that basis: no `license.spdx_id`, no stars, `Trend 61` frozen, and an aggregator's
`~50 000*` for `DeepTutor` refused. All four bounds were SELF-IMPOSED.

`ACTION VV`, registered at `p241` (`intel/open-gaps.md`), already said why:

    "The GitHub search API is 403 via curl and 200 via the MCP server from the
     same environment. Eight passes of 'GitHub Trending went unqueried' may have
     been measuring the TRANSPORT, not the channel."

`p554` tested `curl` alone and generalised from one transport to the channel.
Measured on this session, the five transports are NOT equivalent:

    curl https://api.github.com/repos/{slug}          -> 403
    curl https://github.com/{slug}            (HTML)  -> 403
    gh api repos/{owner}/{repo}                       -> 403  (session repo-bound)
    gh api search/repositories                        -> 403  (path not available)
    MCP search_repositories, `repo:` filtered         -> 200  <-- the channel is HERE

THE WINDOW THIS MODULE READS, DECLARED (`Gap 554-C`'s ask)
----------------------------------------------------------
`554-C` asked that any band declare, in the function that computes it, WHICH
WINDOW it reads and WHY that window is the right bet. The platform field's window
is not ours to choose, and that is the whole point:

    GitHub runs `licensee` over the repository ROOT and emits ONE SPDX id.

One id. Not a set. So the platform channel CANNOT express a composite grant
(`pupilfirst`: CC-BY-SA-4.0 for docs, MIT for JS) or a code/corpus split
(`learning-commons-org/*`: MIT code, CC-BY-NC-SA-4.0 corpora) BY CONSTRUCTION.
When it answers `NOASSERTION` on those, that is the field being HONEST about a
shape it cannot represent -- not a classifier failing. This module therefore
NEVER treats `NOASSERTION` as a tie-breaker, and never as absence.

    `None`         -> no licence file matched at all          -> PLATFORM-SILENT
    `NOASSERTION`  -> a licence file WAS found, unclassified  -> PLATFORM-DECLINES

GitHub distinguishes these two and this base never has. The distinction is the
module's main contribution: `PLATFORM-DECLINES` is positive evidence that an
artefact's grant is non-standard, which is exactly when a reader needs telling.

WHAT IT CANNOT DO
-----------------
1. It is NOT SCRIPTABLE END-TO-END. The harvest arrives through a tool call, not
   a socket a `Makefile` can open. The harvest is committed to `evidence/` and
   this module reads the committed file, so the JOIN is reproducible offline and
   the HARVEST is attested by its commit. A successor re-harvests; it does not
   re-derive.
2. The search index SILENTLY OMITS live repositories (`Gap 504-A`'s standing
   check; 5 of 84 on this pass, all 5 live on `git ls-remote`). An absent row is
   a fact about the INDEX, never about the repository.
"""
import sys

# 🔵 Family-root comparison. The platform writes a bare `GPL-3.0`; a payload read
# by `grant-verdict.py` may carry `GPL-3.0-or-later`. Comparing the raw strings
# would manufacture a disagreement out of an election the platform cannot encode.
# 🔴 The suffix is STRIPPED FOR MATCHING and PRINTED IN FULL, so no reader loses it.
_ELECTIONS = ("-OR-LATER", "-ONLY")


def root(fam):
    """The family root, for comparison only -- never for reporting."""
    u = (fam or "").strip().upper()
    for e in _ELECTIONS:
        if u.endswith(e):
            u = u[: -len(e)]
    return u


def band(platform_spdx, payload_families):
    """🔵 WINDOW: see the module docstring -- `licensee` over the repository root,
    one SPDX id, no composites. 🔴 `NOASSERTION` is never resolved in any
    channel's favour and never counted as silence."""
    p = (platform_spdx or "").strip()
    pay = {root(x) for x in payload_families.split("+") if x and x != "-"}

    if p in ("", "None", "null"):
        return ("PLATFORM-SILENT" if pay else "PLATFORM-AND-PAYLOAD-BOTH-SILENT")
    if p == "NOASSERTION":
        return "PLATFORM-DECLINES"
    if not pay:
        return "PLATFORM-RESOLVES-PAYLOAD-SILENT"
    # 🔴 `Gap 554-D`'s ask, honoured here too: test the MODIFIER, never one literal
    # id. A platform id that drops `-NC` against a payload that carries it is a
    # DISAGREEMENT in the direction that reaches a proposal, so it must not match.
    if "-NC" in root(p) or any("-NC" in f for f in pay):
        if root(p) in pay:
            return "PLATFORM-CONFIRMS-PAYLOAD"
        return "PLATFORM-DISAGREES-WITH-PAYLOAD-ON-NONCOMMERCIAL"
    return ("PLATFORM-CONFIRMS-PAYLOAD" if root(p) in pay
            else "PLATFORM-DISAGREES-WITH-PAYLOAD")


def load_tsv(path, key=0):
    rows, head = {}, None
    for i, line in enumerate(open(path)):
        f = line.rstrip("\n").split("\t")
        if i == 0:
            head = f
            continue
        if len(f) > key and f[key]:
            rows[f[key]] = f
    return head, rows


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        print("usage: platform-channel.py <doc-channel.tsv> <platform-harvest.tsv>")
        return 1
    _, doc = load_tsv(sys.argv[1])
    _, plat = load_tsv(sys.argv[2])

    print("repo\tdoc_verdict\tpayload_families\tplatform_spdx\tstars\tpushed"
          "\tplatform_band\tfour_channel_verdict")
    omitted = []
    for slug, d in sorted(doc.items()):
        doc_v = d[5] if len(d) > 5 else "-"
        payload = d[2] if len(d) > 2 else "-"
        pr = plat.get(slug)
        if pr is None:
            omitted.append(slug)
            print(f"{slug}\t{doc_v}\t{payload}\t-\t-\t-"
                  f"\tPLATFORM-NOT-IN-INDEX\tTHREE-CHANNEL-ONLY")
            continue
        spdx, stars, _branch, pushed = pr[1], pr[2], pr[3], pr[4]
        b = band(spdx, payload)
        # 🔵 The four-channel verdict is deliberately NOT a collapse of the two.
        # It names what a reader must act on, and keeps the doc verdict visible.
        if b == "PLATFORM-DECLINES" and doc_v == "GRANT-DISAGREES-WITH-DOCUMENTATION":
            four = "NON-STANDARD-GRANT-CONFIRMED-BY-PLATFORM-DECLINING"
        elif b == "PLATFORM-DISAGREES-WITH-PAYLOAD":
            four = "FOUR-WAY-SPLIT-ESCALATE"
        elif b.endswith("ON-NONCOMMERCIAL"):
            four = "NONCOMMERCIAL-RISK-ESCALATE"
        elif b == "PLATFORM-CONFIRMS-PAYLOAD" and doc_v == "GRANT-DISAGREES-WITH-DOCUMENTATION":
            four = "PAYLOAD-UPHELD-DOC-IS-THE-OUTLIER"
        elif b == "PLATFORM-AND-PAYLOAD-BOTH-SILENT" and doc_v == "ALL-CHANNELS-SILENT":
            four = "FOUR-CHANNELS-SILENT"
        elif b == "PLATFORM-CONFIRMS-PAYLOAD":
            four = "FOUR-CHANNELS-CONSISTENT"
        else:
            four = b
        print(f"{slug}\t{doc_v}\t{payload}\t{spdx}\t{stars}\t{pushed}\t{b}\t{four}")

    # 🔴 `Gap 504-A`'s STANDING CHECK, run on every call, not on request.
    sys.stderr.write(f"\n[504-A] queried {len(doc)}  joined {len(doc) - len(omitted)}"
                     f"  omitted-by-index {len(omitted)}\n")
    for s in omitted:
        sys.stderr.write(f"[504-A]   omitted: {s}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
