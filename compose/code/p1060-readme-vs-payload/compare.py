#!/usr/bin/env python3
"""`p444/compare.py` — the join that closes `Gap 443-C`.

Reads a `p444/probe.sh` TSV (payload side: path, bytes, sha12, family — produced by
`lib/measure`, so `P834`-proof) plus the README captured at the SAME commit, and emits one
verdict row per repository.

Verdicts, and the only one that costs money is the third:

  NO-README                  no README at the probed commit
  README-SILENT              a README that makes no licence claim at all
  AGREE                      a claim whose family matches the payload family
  🔴 README-MORE-PERMISSIVE  the README's claim is a MORE permissive tier than the payload
  README-MORE-RESTRICTIVE    the README's claim is a LESS permissive tier than the payload
  DIVERGE-SAME-TIER          different spelling, same tier (e.g. README MIT / payload BSD)
  NO-PAYLOAD                 a README claim with no grant file to check it against

`NO-PAYLOAD` is not a clean row.  A repository that claims MIT in prose and ships no
LICENSE has stated a grant it has not made; this base grades that as a claim without a
payload rather than as a permissive row, which is what a README-only reading would do.
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from readme_claim import claims_in, TIER, tier_of  # noqa: E402

LIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lib")


def payload_family(path):
    """Delegate to the shared, `P171`-hardened classifier.  Never reimplemented here."""
    out = subprocess.run([os.path.join(LIB, "measure"), "--family", path],
                         capture_output=True, text=True)
    return out.stdout.strip() if out.returncode == 0 else "MEASURE-FAILED"


# 🟡 An UNVERSIONED claim is a version-unspecified match, not a divergence.  `OS4ED/openSIS-
# Classic` and `francoisjacquet/rosariosis` both say "GPL" in prose against a `GPL-2.0`
# payload; v1 compared the strings, found "GPL" != "GPL-2.0", and reported both.  A README
# that does not state a version has not CONTRADICTED one.
_ROOTS = ("GPL", "BSD", "LGPL", "AGPL", "MPL", "CC-BY", "ODbL", "EPL", "ECL")


def _family_match(claim_fam, payload_fam):
    a, b = _norm(claim_fam), _norm(payload_fam)
    if a == b:
        return True
    # a bare root claim matches any version of that root -- but AGPL/LGPL are their own
    # roots and must not be swallowed by "GPL".
    for root in _ROOTS:
        if a == root and b.startswith(root):
            root_of_b = next((r for r in ("AGPL", "LGPL") if b.startswith(r)), None)
            if root_of_b and root == "GPL":
                return False
            return True
    return False


def _norm(fam):
    """Payload families and README spellings meet here.

    `family_of` emits `BSD` for a payload it grades as the BSD family without committing to
    a clause count; a README that says "BSD-3-Clause" is the same family at the same tier.
    Normalising to the FAMILY ROOT is what makes AGREE mean "same grant", not "same string".
    """
    if fam.startswith("BSD"):
        return "BSD"
    if fam.startswith("LGPL"):
        return "LGPL"
    return fam


# 🔴 THE THIRD DEFECT THIS INSTRUMENT FOUND IN ITSELF — and it was caught by VERIFYING a
# finding before publishing it, which is the only reason it is not a false accusation on a
# live shelf row.
#
# `pengusto/google-classroom-mcp` graded `README-MORE-PERMISSIVE` (README MIT badge, payload
# "Pengusto Commercial License 1.0").  Read first-hand, the README is scrupulously honest:
# the badge says "License: Commercial extensions / MIT upstream", a "Licensing before use"
# section states the split, and a "License and attribution" section says outright that the
# two licences cover different parts and "are not alternative licenses for the whole
# project".  The tree carries BOTH `LICENSE` and `LICENSES/MIT-upstream.txt`.
#
# 🔵 The defect is `min(claims, key=tier)` — "the most permissive thing the README claims is
# what a reader takes away".  That is right for a README with ONE grant and wrong for one
# that SCOPES each grant to a different part of the tree.  A dual-grant declaration is a
# correct README, not a misleading one.
def verdict(claims, fam, n_grants=1, tree_fams=None):
    if fam in ("NO-PAYLOAD", "-", ""):
        return ("NO-PAYLOAD" if claims else "README-SILENT"), ""
    if not claims:
        return "README-SILENT", ""
    if any(_family_match(c.family, fam) for c in claims):
        return "AGREE", ""
    # A claim satisfied by ANY grant in the tree is satisfied.  `p442`: the root row is not
    # the whole grant, so the root family is not the whole answer either.
    if tree_fams:
        for c in claims:
            for tf in tree_fams:
                if _family_match(c.family, tf):
                    return ("DUAL-GRANT-DECLARED" if n_grants >= 2 else "AGREE"), \
                        f"README={c.family} matched by a non-root grant in a {n_grants}-grant tree"
    if n_grants >= 2 and len({c.family for c in claims}) >= 2:
        fams = ",".join(sorted({c.family for c in claims}))
        return "DUAL-GRANT-DECLARED", f"README declares {fams}; tree carries {n_grants} grant paths"
    ptier = tier_of(fam)
    if ptier is None:
        # The map, not the repository, is what is missing.  Say so.
        best = min(claims, key=lambda c: c.tier)
        return "PAYLOAD-FAMILY-UNMAPPED", f"README={best.family} payload={fam} (no tier for payload)"
    # The most permissive thing the README claims is what a reader takes away.
    best = min(claims, key=lambda c: c.tier)
    detail = f"README={best.family}({best.tier}/{best.context}) payload={fam}({ptier})"
    if best.tier < ptier:
        return "README-MORE-PERMISSIVE", detail
    if best.tier > ptier:
        return "README-MORE-RESTRICTIVE", detail
    return "DIVERGE-SAME-TIER", detail


def read_readme(outdir, slug):
    p = os.path.join(outdir, "payloads", slug.replace("/", "_") + "__READMEFILE")
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _anchor(grants):
    """The project's OWN grant among every grant path in its tree."""
    # 🔴 A FIFTH one, same run.  `is_licence_path` grades `assets/notice.png` as a grant
    # path — correctly, by its `notice.*` glob, which exists for real NOTICE files — and a
    # depth-only rank then preferred that PNG over `docs/License.txt` on an alphabetical
    # tiebreak.  `OS4ED/openSIS-Classic` and `francoisjacquet/rosariosis` both anchored on
    # an UNCLASSIFIED payload and reported their READMEs as diverging from a picture.
    # 🔵 An anchor must prefer a payload the classifier could actually READ.  Unclassifiable
    # payloads sort last; they are evidence the PATH matched, not that a GRANT was found.
    unreadable = {"UNCLASSIFIED", "NO-PAYLOAD", "MEASURE-FAILED", "FETCH-FAILED", "-", ""}

    def rank(g):
        path, fam = g[0], g[1]
        depth = path.count("/")
        return (1 if fam in unreadable else 0, 0 if depth == 0 else 1, depth, path.lower())
    return sorted(grants, key=rank)[0]


def main():
    if len(sys.argv) < 2:
        print("usage: compare.py <probe-outdir>", file=sys.stderr)
        return 2
    outdir = sys.argv[1]
    tsv = os.path.join(outdir, "probe.tsv")
    # 🔴 THE FOURTH DEFECT, and it is `p442`'s lesson arriving in this instrument's join.
    #
    # v1 kept ONE row per repository, "anchored on the ROOT grant when there is one", and
    # fell back to whichever row happened to come last.  Measured on the shelf, that
    # produced two false findings out of three:
    #
    #   pengusto/google-classroom-mcp  tree = LICENSE (non-OSI) + LICENSES/MIT-upstream.txt
    #                                  (MIT).  The README's MIT claim IS satisfied by a
    #                                  grant in the tree; anchoring on the root hid it.
    #   OS4ED/openSIS-Classic          11 grant paths, 9 of them VENDORED (ckeditor,
    #                                  htmlpurifier, codemirror).  The project's OWN grant
    #                                  is `docs/License.txt` GPL-2.0 — which matches its
    #                                  README — but a vendored `MPL-1.1` came last and won.
    #
    # 🔵 So a README claim is checked against the SET of families in the tree, and the
    # ANCHOR for a tier comparison is the project's own grant: a root-level path first,
    # then the shallowest path, with `assets/js/plugins/`-style vendoring deprioritised.
    # `is_bundled` is a floor and not a proof (lib README, `T229-M2`), so depth is the
    # tiebreak rather than a path vocabulary this instrument would have to re-guess.
    rows = {}
    with open(tsv) as fh:
        next(fh)
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) < 8:
                continue
            slug, path, fam = f[0], f[4], f[7]
            try:
                ngr = int(f[3])
            except (ValueError, IndexError):
                ngr = 1
            e = rows.setdefault(slug, {"head": f[1], "ngr": ngr, "grants": []})
            e["grants"].append((path, fam, f[5], f[6]))


    print("slug\thead_sha\tgrant_path\tbytes\tsha12\tpayload_family\tclaims\tverdict\tdetail")
    for slug, e in rows.items():
        head, ngr, grants = e["head"], e["ngr"], e["grants"]
        path, fam, byt, sha = _anchor(grants)
        tree_fams = {g[1] for g in grants}
        text = read_readme(outdir, slug)
        if text is None:
            print(f"{slug}\t{head[:12]}\t{path}\t{byt}\t{sha}\t{fam}\t-\tNO-README\t")
            continue
        allc = claims_in(text, slug)
        # FOREIGN claims are not this repository's claims.  Dropped from the verdict and
        # reported separately, so a boilerplate README reads as SILENT-with-a-reason rather
        # than as a grant the repository never made.
        cs = [c for c in allc if not c.context.startswith("FOREIGN")]
        foreign = [c for c in allc if c.context.startswith("FOREIGN")]
        v, detail = verdict(cs, fam, ngr, tree_fams)
        if foreign and not cs:
            detail = (detail + " " if detail else "") + \
                "dropped-foreign=" + ",".join(f"{c.family}:{c.context}" for c in foreign)
        cl = ",".join(f"{c.family}:{c.context}" for c in allc) or "-"
        print(f"{slug}\t{head[:12]}\t{path}\t{byt}\t{sha}\t{fam}\t{cl}\t{v}\t{detail}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
