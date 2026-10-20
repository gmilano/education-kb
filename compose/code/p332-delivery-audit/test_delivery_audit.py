#!/usr/bin/env python3
"""p332 controls — offline, no network, safe in a hook.

Every case below was a real false positive or a real false negative measured against this
repository's own corpus during p332, not an invented example. The comment on each names it.
"""
import importlib.util
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("da", os.path.join(HERE, "delivery_audit.py"))
da = importlib.util.module_from_spec(spec)
spec.loader.exec_module(da)

N = 0
FAIL = []


def ok(cond, label):
    global N
    N += 1
    if not cond:
        FAIL.append(label)


# ---- slug_fields: the harvester's precision ------------------------------------------------
ok(da.slug_fields("lti-tool/lti-tool\tMIT") == ["lti-tool/lti-tool"],
   "a real slug in field 1 is harvested")
ok(da.slug_fields("JuliaPluto/Pluto.jl\tMIT") == ["JuliaPluto/Pluto.jl"],
   "a dot-extension repo name survives intact — the p250 truncation class")
# measured: `repos/trending.md` was harvested 175 times as a slug before DENY_FIRST grew
ok(da.slug_fields("repos/trending.md\tx") == [], "a shelf path is not a slug")
ok(da.slug_fields("agents/top.md\tx") == [], "agents/top.md is not a slug")
ok(da.slug_fields("compose/patterns.md\tx") == [], "compose/patterns.md is not a slug")
# measured: `n/a` was the single highest-sighting 'slug' in the corpus at 205 sightings
ok(da.slug_fields("n/a\tMIT") == [], "the empty-cell spelling n/a is not a slug")
ok(da.slug_fields("s/n\tMIT") == [], "the empty-cell spelling s/n is not a slug")
ok(da.slug_fields("main/LICENSE\tx") == [], "a ref/path pair is not a slug")
ok(da.slug_fields("schemas/lti13/ags\tx") == [], "a three-segment path is not a slug")
ok(da.slug_fields("raw.githubusercontent.com/a\tx") == [], "a hostname is not an owner")
ok(da.slug_fields("npm/core\tx") == [], "a registry name is not an owner")
ok(da.slug_fields("a/b\tx") == [], "one-character segments are below the slug floor")
# .git is a clone-URL spelling of the SAME repository, not a different row
ok(da.slug_fields("Cvmcosta/ltijs.git\tx") == ["Cvmcosta/ltijs"],
   "a .git clone spelling normalises onto the repository")
ok(da.slug_fields("owner/repo\tMIT\tother/thing") == ["owner/repo", "other/thing"],
   "every slug-shaped field is harvested, not just the first")

# ---- fold ---------------------------------------------------------------------------------
ok(da.fold("OpenOLAT/OpenOLAT") == "openolat/openolat", "fold lowercases")
ok(da.fold("owner/repo)") == "owner/repo", "fold strips trailing prose punctuation")

# ---- grant classification -----------------------------------------------------------------
ok(da.classify_grant("x\tMIT\tfoo") == "permissive", "MIT is permissive")
ok(da.classify_grant("x\tApache-2.0") == "permissive", "Apache is permissive")
ok(da.classify_grant("x\tAGPL-3.0") == "copyleft", "AGPL is copyleft")
ok(da.classify_grant("x\tODbL-1.0") == "copyleft", "ODbL is copyleft")
ok(da.classify_grant("x\tMIT code; corpora CC BY-SA 4.0") == "mixed",
   "MIT code beside a share-alike corpus is mixed — the os-taxonomy shape")
ok(da.classify_grant("x\tno licence file") == "ungranted", "a stated absence is ungranted")
ok(da.classify_grant("x\tsomething else") == "unknown", "silence is not a grant")

# ---- disposition --------------------------------------------------------------------------
ok(da.classify_disposition("x\tunplaced\ty") == "pending",
   "`unplaced` is the deferral marker — the lti-tool cell p331 found")
ok(da.classify_disposition("x\tDEAD — seven years") == "refused", "dead is a recorded refusal")
ok(da.classify_disposition("x\tbelow bar") == "refused", "below bar is a recorded refusal")
ok(da.classify_disposition("x\tMIT\t1066") == "silent", "no marker is silence, not refusal")
ok(da.classify_disposition("x\tunplaced\tdead") == "pending",
   "pending outranks refused: a cell carrying both is still deferred")

# ---- truncation predicate -----------------------------------------------------------------
tr = da.truncations({"dmitry-viskov/pylti1", "dmitry-viskov/pylti1.3"})
ok(tr == {"dmitry-viskov/pylti1": ["dmitry-viskov/pylti1.3"]},
   "a bare prefix of a dot-extension slug is flagged")
# p250's ACTION XN named its own falsifier and p332 measured it: BOTH of these resolve
ok(da.truncations({"touchrefletz/maia", "touchrefletz/maia.edu"}) == {},
   "ACTION XN's falsifier: TouchRefletz/maia is real, so the prefix rule must not fire")
ok(da.truncations({"autolab/autolab", "autolab/autolab.github.io"}) == {},
   "autolab/autolab is real beside its .github.io — measured p332")
ok(da.truncations({"a/b", "c/d"}) == {}, "unrelated slugs are not flagged")

# ---- harvest_evidence ---------------------------------------------------------------------
with tempfile.TemporaryDirectory() as td:
    ev = os.path.join(td, "evidence")
    os.makedirs(ev)
    with open(os.path.join(ev, "x.2026-01-01-p1.tsv"), "w") as fh:
        fh.write("# owner/comment-slug is prose about the pass, not a measurement\n")
        fh.write("\n")
        fh.write("real/row\tMIT\tunplaced\n")
    got = da.harvest_evidence(td)
    ok("real/row" in got, "a measurement row is harvested")
    ok("owner/comment-slug" not in got, "a # header line is prose, not a measurement")
    ok(got["real/row"][0][2] == "permissive", "the grant travels with the sighting")
    ok(got["real/row"][0][3] == "pending", "the disposition travels with the sighting")
    ok(da.harvest_evidence(os.path.join(td, "nope")) == {},
       "a missing evidence dir is empty, not fatal — this must run from a partial checkout")

# ---- the control exclusion ----------------------------------------------------------------
ok("decoylex/ltix" in da.CONTROLS,
   "p208's seeded decoy is excluded: it was the top 'defect' at 25 sightings")

# ---- rank ---------------------------------------------------------------------------------
rows = [
    {"slug": "r/refused", "grant": "permissive", "disposition": "refused", "sightings": 9},
    {"slug": "p/pending", "grant": "permissive", "disposition": "pending", "sightings": 1},
    {"slug": "s/silent", "grant": "permissive", "disposition": "silent", "sightings": 9},
]
ok([r["slug"] for r in da.rank(rows)] == ["p/pending", "s/silent", "r/refused"],
   "a recorded refusal ranks last: it is the audit working, not a defect")
ok(da.rank([
    {"slug": "a/copyleft", "grant": "copyleft", "disposition": "pending", "sightings": 1},
    {"slug": "b/perm", "grant": "permissive", "disposition": "pending", "sightings": 1},
])[0]["slug"] == "b/perm", "within a disposition, a permissive grant ranks first")


# ---------------------------------------------------------------- p333: token boundaries
# Every case below is a REAL carrier measured in this repository's `evidence/` at p333, not an
# invented example. The counts in delivery_audit.py's comment block come from the same sweep.

# The wild case that proved the defect: p154 recorded this row's grant CORRECTLY as AGPL-3.0,
# and the bare-substring test read it back as permissive because the evidence FILENAME it
# cites contains `isc` inside `api-di(sc)overy-overlap`.
ok(da.classify_grant(
    "pdfmathtranslate/pdfmathtranslate\tAGPL-3.0\tapi-discovery-overlap.2026-10-12-p154.tsv")
   == "copyleft",
   "an AGPL row citing api-discovery-overlap is copyleft, not permissive (`isc` in `discovery`)")

# p329's activity vocabulary. `commits` and `committed` entered these shelves as a MEASUREMENT
# and silently re-graded the grant column one pass later.
for carrier in ("2,935 commits", "committed yesterday", "733 commits / 127 authors",
                "last commit 2026-10-19"):
    ok(da.classify_grant("x/y\t" + carrier) == "unknown",
       f"p329's activity vocabulary is not a grant: {carrier!r}")

# The owner name. `dmitry-viskov/pylti1.3` is measured 32 times in this corpus.
ok(da.classify_grant("dmitry-viskov/pylti1.3\tno grant read") != "permissive",
   "a maintainer's first name is not a licence (`mit` in `dmitry`)")

# The remaining measured carriers, each an English word that is not a grant.
for carrier in ("discharged", "disclosure", "committee", "permitted", "rate_limit",
                "rick-254/moodle-quizsmith", "mitigation", "apachecon"):
    ok(da.classify_grant("x/y\t" + carrier) == "unknown",
       f"{carrier!r} contains a licence token and is not a licence claim")

# The other direction matters just as much: the boundary rule must not discard real spellings.
# The one-letter right-hand allowance exists for exactly these two.
ok(da.classify_grant("x/y\tGPLv3") == "copyleft", "GPLv3 is a real spelling and must survive")
ok(da.classify_grant("x/y\tMPL-2.0") == "permissive", "MPL-2.0 must survive the boundary rule")
for spelling, want in (("MIT License", "permissive"), ("Apache License 2.0", "permissive"),
                       ("BSD-3-Clause", "permissive"), ("CC0-1.0", "permissive"),
                       ("ISC License", "permissive"), ("AGPL-3.0", "copyleft"),
                       ("LGPL-2.1", "copyleft"), ("CC BY-SA 4.0", "copyleft"),
                       ("apache2", "permissive"), ("mit-license", "permissive")):
    ok(da.classify_grant("x/y\t" + spelling) == want,
       f"{spelling} still grades {want}")

# p332's own control must still hold: MIT code beside a share-alike corpus is `mixed`, and the
# compound branch must be reachable through the new matcher too.
ok(da.classify_grant("withmarbleapp/os-taxonomy\tMIT code; corpora CC BY-SA 4.0") == "mixed",
   "the mixed branch survives the boundary rule (p332's os-taxonomy shape)")

# UNGRANTED is still tested first, so `unlicensed` never reads as the Unlicense.
ok(da.classify_grant("x/y\tunlicensed") == "ungranted",
   "`unlicensed` is an absence, not the Unlicense")

# The self-ingestion guard. The audit's own output is derived, not measured.
ok(any(d in "p332-delivery-audit.2026-10-20-p332.tsv" for d in da.DERIVED_EVIDENCE),
   "the audit's own output is named as derived evidence")
ok(not any(d in "api-discovery-overlap.2026-10-12-p154.tsv" for d in da.DERIVED_EVIDENCE),
   "a real measurement file is not excluded as derived")

_tmp = tempfile.mkdtemp()
os.makedirs(os.path.join(_tmp, "evidence"))
with open(os.path.join(_tmp, "evidence", "real-census.2026-01-01-p1.tsv"), "w") as fh:
    fh.write("owner/kept\tMIT\n")
with open(os.path.join(_tmp, "evidence", "p999-delivery-audit.2026-01-01-p999.tsv"), "w") as fh:
    fh.write("owner/derived\tMIT\n")
_h = da.harvest_evidence(_tmp)
ok("owner/kept" in _h, "a measurement file is harvested")
ok("owner/derived" not in _h, "the audit does not re-ingest its own output")

print(f"p332-delivery-audit: {N - len(FAIL)}/{N} controls pass")
for f in FAIL:
    print(f"  FAIL: {f}")
sys.exit(1 if FAIL else 0)
