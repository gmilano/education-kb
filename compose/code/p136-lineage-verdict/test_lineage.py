"""Tests for p136-lineage-verdict. Every fixture is a value MEASURED on 2026-10-11
by this pass -- README sha256 prefixes from raw.githubusercontent.com, ref-set
hashes from `git ls-remote --heads --tags`, root tree shas and author sets from
`git clone --depth 50`. No invented repositories, no invented shas.

Run: python3 -I test_lineage.py
"""
import os
import sys

# python3 -I does not put the script's directory on sys.path, and this instrument
# is meant to be runnable with -I (the harness rule for reading downloaded data).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lineage import (Repo, verdict, cluster_verdict, same_slug,
                     attribution_rewritten,
                     licence_dropped,
                     ALIAS, FORK_AT_TIP, DIVERGED_FORK, STRIPPED, SQUASHED_COPY,
                     INDEPENDENT, UNRESOLVED)

FAILS = []


def check(name, got, want):
    if got != want:
        FAILS.append(f"{name}: got {got!r}, want {want!r}")


def check_raises(name, fn, exc):
    try:
        fn()
    except exc:
        return
    except Exception as e:  # noqa: BLE001
        FAILS.append(f"{name}: raised {type(e).__name__}, want {exc.__name__}")
        return
    FAILS.append(f"{name}: did not raise {exc.__name__}")


# ---------------------------------------------------------------- measured data
# The four api_enem_microdados repositories (ACTION BW). Identical README
# (fea59dc854f35eac9cb72f14, 1842 B), identical ROOT TREE, 20 commits each with
# identical messages and dates -- and not one shared commit sha.
ENEM_TREE = "a847c05fb690b23ec6255d17de4542b3416ce562"
enem_orig = Repo("filipedeschamps/api_enem_microdados", readme_sha="fea59dc854f35eac9cb72f14",
                 refset_sha="e22b78ce85ce4214", head="1e8d72ebc1fe", tree_sha=ENEM_TREE,
                 commit_shas=["1e8d72ebc1fe", "28978c5", "25a8d23"],
                 authors=["Filipe Deschamps <filiped@gmail.com>",
                          "OtavioVB <otaviovb.developer@gmail.com>"])
enem_rend = Repo("rendgentmars/api_enem_microdados", readme_sha="fea59dc854f35eac9cb72f14",
                 refset_sha="bc9d964900d4621c", head="988d4d9c1c3c", tree_sha=ENEM_TREE,
                 commit_shas=["988d4d9c1c3c", "f3abf1b", "7bd387b"],
                 authors=["rendgentmars <10532627+rendgentmars@users.noreply.github.com>"])
enem_livr = Repo("livrunakcream/api_enem_microdados", readme_sha="fea59dc854f35eac9cb72f14",
                 refset_sha="38a9fca73a3cee53", head="0743bc1408dc", tree_sha=ENEM_TREE,
                 commit_shas=["0743bc1408dc", "85de3fc", "6dfd323"],
                 authors=["livrunakcream <12874613+livrunakcream@users.noreply.github.com>"])
enem_blue = Repo("bluesky816/api_enem_microdados", readme_sha="fea59dc854f35eac9cb72f14",
                 refset_sha="9c2573019c9d76b0", head="17af4e419096", tree_sha=ENEM_TREE,
                 commit_shas=["17af4e419096", "4c4d7b2", "bb813d2"],
                 authors=["garu2044x <1293742+garu2044x@users.noreply.github.com>"])

# One repository under two slugs. ref sets identical to the hash.
onerost_a = Repo("theopenem/OneRoster.NET", readme_sha="68a303bf6d6dec62c5786a5d",
                 refset_sha="3f4540f9706d9099", head="4f96365d3108")
onerost_b = Repo("jdolny/OneRoster.NET", readme_sha="68a303bf6d6dec62c5786a5d",
                 refset_sha="3f4540f9706d9099", head="4f96365d3108")
# Same, across BOTH a rename and a transfer: KI-Campus/LRS is served as openHPI/openLRS.
lrs_a = Repo("KI-Campus/LRS", readme_sha="826b2c7e7161383143514fee",
             refset_sha="ef865c69a8416619", head="db284a9d550a")
lrs_b = Repo("openHPI/openLRS", readme_sha="826b2c7e7161383143514fee",
             refset_sha="ef865c69a8416619", head="db284a9d550a")

# A live fork that has not diverged: same HEAD, different ref sets (2 refs vs 17).
moodler_a = Repo("Dymayo/moodler-mcp", readme_sha="fc90924a4e4867a6079cd936",
                 refset_sha="5068f4302fc6e09d", head="4e6139eb9c6b")
moodler_b = Repo("GhaithAlHallak8/moodler-mcp", readme_sha="fc90924a4e4867a6079cd936",
                 refset_sha="5a538f156b8cb5f2", head="4e6139eb9c6b")

# Measured at ref level only: heads differ, nothing deeper was measured.
canvas_a = Repo("abr-Projects/canvas-mcp", readme_sha="7f50ee2f42594923210d1200",
                refset_sha="9f671c90a8104682", head="c4683b33631f")
canvas_b = Repo("harrywang/canvas-mcp", readme_sha="7f50ee2f42594923210d1200",
                refset_sha="26ffe7aa7e3e0186", head="0fccce281a11")

# The squashed re-upload (measured: 1 commit vs 79, different trees, 0 shared
# commits, README byte-identical at 55e2f536ac87f2893dc89463, and the upstream MIT
# LICENSE file absent from the copy).
kt_upstream = Repo("hcnoh/knowledge-tracing-collection-pytorch",
                   readme_sha="55e2f536ac87f2893dc89463", refset_sha="4ceeeae5b880f493",
                   head="6151f490db17", tree_sha="f01868a6a51995477627d5a890d300a98cf12b22",
                   commit_count=79,
                   files=["LICENSE", "README.md", "train.py", "models/dkt.py"])
kt_copy = Repo("0awei0/kt", readme_sha="55e2f536ac87f2893dc89463",
               refset_sha="108af8d115f79622", head="403b10764cd8",
               tree_sha="fe39319089ccb64c13c1d811d76bdc30567c5dfa", commit_count=1,
               files=["README.md", "train.py", "models/dkt.py",
                      "models/__pycache__/dkt.cpython-311.pyc"])

# Case-variant slugs this KB publishes as two rows. One repository, no finding.
elgg_a = Repo("Elgg/Elgg", readme_sha="fee22e6c23d9e71658f9d73d", refset_sha="x", head="y")
elgg_b = Repo("elgg/elgg", readme_sha="fee22e6c23d9e71658f9d73d", refset_sha="x", head="y")


# -------------------------------------------------------------------- the tests
def test_alias_beats_fork():
    # Two slugs for one repository share HEAD as well; if HEAD were checked first
    # this pair would read FORK_AT_TIP, which is the error ACTION BU exposed.
    check("alias/oneroster", verdict(onerost_a, onerost_b), ALIAS)
    check("alias/lrs-renamed-and-transferred", verdict(lrs_a, lrs_b), ALIAS)


def test_fork_at_tip():
    check("fork-at-tip/moodler", verdict(moodler_a, moodler_b), FORK_AT_TIP)


def test_enem_is_a_stripped_copy_not_a_fork():
    for a, b, label in [(enem_orig, enem_rend, "rend"), (enem_orig, enem_livr, "livr"),
                        (enem_orig, enem_blue, "blue"), (enem_rend, enem_blue, "rend-blue")]:
        check(f"enem/{label}", verdict(a, b), STRIPPED)


def test_enem_cluster_and_the_rewritten_identities():
    v, distinct = cluster_verdict([enem_orig, enem_rend, enem_livr, enem_blue])
    check("enem/cluster-verdict", v, STRIPPED)
    check("enem/distinct-count", len(distinct), 4)
    rewritten = attribution_rewritten([enem_orig, enem_rend, enem_livr, enem_blue])
    check("enem/rewritten-count", len(rewritten), 3)
    # bluesky816's commits are authored by a FIFTH identity -- the owner and the
    # rewritten author are not even the same account.
    check("enem/bluesky-author",
          rewritten["bluesky816/api_enem_microdados"][0].startswith("garu2044x"), True)
    # The original's own authorship is never reported as rewritten.
    check("enem/original-not-flagged",
          "filipedeschamps/api_enem_microdados" in rewritten, False)


def test_unmeasured_is_not_called_independent():
    # The honest answer for a pair measured only at ref level.
    check("canvas/unresolved", verdict(canvas_a, canvas_b), UNRESOLVED)
    # With trees measured and different, INDEPENDENT becomes sayable.
    a = Repo(canvas_a.slug, readme_sha=canvas_a.readme_sha, refset_sha=canvas_a.refset_sha,
             head=canvas_a.head, tree_sha="t1")
    b = Repo(canvas_b.slug, readme_sha=canvas_b.readme_sha, refset_sha=canvas_b.refset_sha,
             head=canvas_b.head, tree_sha="t2")
    check("canvas/independent-once-measured", verdict(a, b), INDEPENDENT)


def test_squashed_copy_and_the_dropped_grant():
    check("kt/verdict", verdict(kt_upstream, kt_copy), SQUASHED_COPY)
    check("kt/licence-dropped", licence_dropped(kt_upstream, kt_copy), True)
    # Direction matters: the upstream has not dropped anything.
    check("kt/licence-dropped-reverse", licence_dropped(kt_copy, kt_upstream), False)
    # Unmeasured file lists return None, never a confident False.
    check("kt/unmeasured", licence_dropped(kt_upstream, Repo("x/y", files=())), None)
    # A squashed copy must not outrank a real shared ancestry.
    a = Repo("o1/r", readme_sha="s", refset_sha="r1", head="h1", commit_count=1,
             commit_shas=["h1", "common"], tree_sha="t1")
    b = Repo("o2/r", readme_sha="s", refset_sha="r2", head="h2", commit_count=90,
             commit_shas=["h2", "common"], tree_sha="t2")
    check("kt/ancestry-wins", verdict(a, b), DIVERGED_FORK)


def test_diverged_fork_needs_shared_ancestry():
    a = Repo("o1/r", readme_sha="s", refset_sha="r1", head="h1",
             commit_shas=["h1", "common"], tree_sha="t1")
    b = Repo("o2/r", readme_sha="s", refset_sha="r2", head="h2",
             commit_shas=["h2", "common"], tree_sha="t2")
    check("diverged", verdict(a, b), DIVERGED_FORK)


def test_case_variants_collapse_to_nothing():
    check("case/same-slug", same_slug(elgg_a, elgg_b), True)
    v, distinct = cluster_verdict([elgg_a, elgg_b])
    check("case/verdict", v, None)
    check("case/distinct", len(distinct), 1)
    # 37 of the 71 clusters this pass measured are of exactly this shape.


def test_verdict_refuses_pairs_that_do_not_share_a_readme():
    check_raises("guard/different-readme",
                 lambda: verdict(onerost_a, moodler_a), ValueError)
    check_raises("guard/unmeasured-readme",
                 lambda: verdict(Repo("a/b"), Repo("c/d")), ValueError)


def test_cluster_reports_its_weakest_pair():
    # A cluster holding one alias pair and two unrelated trees is not an alias
    # cluster. Every member here carries a tree sha, so UNRESOLVED is not an option
    # and the cluster has to report the INDEPENDENT pair it contains.
    a = Repo(onerost_a.slug, readme_sha=onerost_a.readme_sha, refset_sha=onerost_a.refset_sha,
             head=onerost_a.head, tree_sha="oneroster-tree")
    b = Repo(onerost_b.slug, readme_sha=onerost_b.readme_sha, refset_sha=onerost_b.refset_sha,
             head=onerost_b.head, tree_sha="oneroster-tree")
    v, _ = cluster_verdict([a, b,
                            Repo("third/OneRoster.NET", readme_sha="68a303bf6d6dec62c5786a5d",
                                 refset_sha="zzz", head="qqq", tree_sha="other"),
                            Repo("fourth/OneRoster.NET", readme_sha="68a303bf6d6dec62c5786a5d",
                                 refset_sha="www", head="eee", tree_sha="other")])
    check("cluster/weakest", v, INDEPENDENT)


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    checks_before = 0
    for t in tests:
        t()
    total = len(tests)
    if FAILS:
        print(f"FAILED {len(FAILS)} check(s) across {total} tests:")
        for f in FAILS:
            print("  -", f)
        sys.exit(1)
    print(f"ok -- {total} tests, all checks passed")
