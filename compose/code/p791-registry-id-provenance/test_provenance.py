#!/usr/bin/env python3
"""P791 offline control. No network. Run: python3 -I test_provenance.py

The suite's job is to hold ONE line down: a code returned by a TARGET id is never a statement
about the HOST. Pass 61 and pass 62 each wrote one into the oracle map, and the fixture below is
the row that produced both.
"""
import os
import sys

# `python3 -I` implies `-P`, which strips the script's own directory from sys.path. `p355`
# (cwd-portability) is the same lesson for the working directory: an instrument that only runs
# one invocation away is an instrument the next pass will not run. Both are fixed here.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from verdict import host_verdict, id_provenance, ref_provenance, rows_with  # noqa: E402

P, F = [], []


def ok(name, got, want):
    (P if got == want else F).append(name)
    if got != want:
        print(f"  FAIL {name}\n    got  {got!r}\n    want {want!r}")


def row(**kw):
    base = dict(slug="x/y", default_ref="main", head_sha="-", served_at="main",
                tree_name="-", declared_license="-",
                tree_name_http="-", guessed_http="-", pub_name="-", pub_repo="-", pub_dir="-",
                pub_maintainer="-", latest="-", latest_time="-", probe_kind="guessed")
    base.update(kw)
    return base


# ---- 1. a host line comes from a PAIR or it does not come at all -------------------------
ok("host/discriminating", host_verdict("200", "404")[0], "REACHABLE-DISCRIMINATING")
ok("host/unreachable", host_verdict("000", "000")[0], "UNREACHABLE")
ok("host/not-discriminating", host_verdict("200", "200")[0], "REACHABLE-NOT-DISCRIMINATING")
ok("host/indeterminate-404-404", host_verdict("404", "404")[0], "INDETERMINATE")
# the shape of the defect: pass 61/62 had ONE code and no pair. There is no call that takes one.
try:
    host_verdict("404")  # noqa
    ok("host/refuses-single-code", "accepted one code", "must require a pair")
except TypeError:
    ok("host/refuses-single-code", "requires a pair", "requires a pair")

# ---- 2. the pass-61/62 row, with the codes measured 2026-10-08 ---------------------------
PACKBACK = row(
    slug="packbackbooks/lti-1-3-php-library", default_ref="master", served_at="master",
    head_sha="a20c71b",
    tree_name="packbackbooks/lti-1p3-tool", declared_license="Apache-2.0",
    tree_name_http="200", guessed_http="404",
    pub_name="packbackbooks/lti-1p3-tool",
    pub_repo="packbackbooks/lti-1-3-php-library",     # slug-normalised, see P792 below
    pub_maintainer="packback", latest="v6.4.4", latest_time="2026-09-23T21:17:20+00:00",
    probe_kind="declared+guessed")
ok("packback/provenance", id_provenance(PACKBACK)[0], "FALSE-ABSENCE-RISK")
ok("packback/ref", ref_provenance(PACKBACK)[0], "DEFAULT-IS-NAMED")

# ---- 3. p253's gate, REUSED: the slug-shaped guess alone decides nothing -----------------
GUESS_ONLY = row(slug="packbackbooks/lti-1-3-php-library",
                 tree_name="-", tree_name_http="404", guessed_http="404", probe_kind="guessed")
from identity import package_identity  # noqa: E402  the imported instrument, not a copy
ok("p253/guess-404-is-undetermined", package_identity(GUESS_ONLY)[0], "UNDETERMINED")
ok("p253/guess-200-is-undetermined",
   package_identity(row(tree_name="-", tree_name_http="200", probe_kind="guessed"))[0],
   "UNDETERMINED")
# and with the declaration present it lands, pointing back at the slug
ok("p253/declared-lands-at-root", package_identity(PACKBACK)[0], "PUBLISHED-AT-ROOT")

# ---- 3b. `P792` — the SEAM between a gate and its own probe layer -------------------------
# Measured end to end this pass: `sh p253/sweep_identity.sh ltijs` emits
#     pub_repo = git+https://github.com/Cvmcosta/ltijs.git
# and `p253/identity.py` compares that string to the slug `Cvmcosta/ltijs`, so it returns
# PUBLISHED-BY-OTHER — "points at ... not at Cvmcosta/ltijs" — for a package pointing at
# exactly that repository. Neither half is wrong on its own; they disagree about the SHAPE of
# the one field they share, and `p253`'s committed TSV escaped it only because its `pub_repo`
# column was hand-normalised to slugs and the script was never changed to match.
LTIJS_RAW = row(slug="Cvmcosta/ltijs", tree_name="ltijs", tree_name_http="200",
                pub_name="ltijs", pub_repo="git+https://github.com/Cvmcosta/ltijs.git",
                pub_maintainer="cvmcosta", probe_kind="declared+registry")
ok("p792/url-shaped-pub_repo-misfires",
   package_identity(LTIJS_RAW)[0], "PUBLISHED-BY-OTHER")
LTIJS_SLUG = dict(LTIJS_RAW, pub_repo="Cvmcosta/ltijs")
ok("p792/slug-shaped-pub_repo-lands", package_identity(LTIJS_SLUG)[0], "PUBLISHED-AT-ROOT")
# and the normaliser this layer applies is what closes the gap, for both URL spellings npm uses
import re  # noqa: E402


def _slug(u):
    m = re.search(r"github\.com[:/]+([^/]+)/([^/.]+)", str(u or "-"))
    return "%s/%s" % (m.group(1), m.group(2)) if m else str(u or "-")


ok("p792/normalise-git-plus-https",
   _slug("git+https://github.com/Cvmcosta/ltijs.git"), "Cvmcosta/ltijs")
ok("p792/normalise-plain-https",
   _slug("https://github.com/packbackbooks/lti-1-3-php-library"),
   "packbackbooks/lti-1-3-php-library")
ok("p792/normalise-ssh", _slug("git@github.com:h5p/h5p-php-library.git"), "h5p/h5p-php-library")
ok("p792/normalise-leaves-non-github-alone", _slug("https://gitlab.com/a/b"),
   "https://gitlab.com/a/b")
ok("p792/normalise-absent", _slug("-"), "-")

# ---- 4. the other direction, which `P788` calls the worse one ----------------------------
ok("provenance/false-presence",
   id_provenance(row(slug="a/b", tree_name="vendor/other", tree_name_http="404",
                     guessed_http="200", probe_kind="declared+guessed"))[0],
   "FALSE-PRESENCE-RISK")

# ---- 5. controls: the cases where no misread is possible ---------------------------------
ok("provenance/id-equals-slug",
   id_provenance(row(slug="monolog/monolog", tree_name="monolog/monolog",
                     tree_name_http="200", guessed_http="200",
                     probe_kind="declared+guessed"))[0], "ID-EQUALS-SLUG")
ok("provenance/no-declaration",
   id_provenance(row(tree_name="-", guessed_http="404"))[0], "NO-DECLARATION")
ok("provenance/agrees",
   id_provenance(row(tree_name="v/p", tree_name_http="200", guessed_http="200",
                     probe_kind="declared+guessed"))[0], "AGREES")
ok("ref/no-manifest", ref_provenance(row(served_at="-"))[0], "NO-MANIFEST-FOUND")
ok("ref/default-is-named", ref_provenance(row(default_ref="main", served_at="main"))[0],
   "DEFAULT-IS-NAMED")

# ---- 5b. `P793` — the three rows this pass measured, each served from a ref it did not name ---
# `raw` 404s `main` and 404s an invented name, but serves the DEFAULT branch for `master`.
# So "read at master" is not provenance, and the oracle is `ls-remote --symref … HEAD`.
for slug, dref, sha in (("php-xapi/client", "0.7", "b39735b"),
                        ("tl-its-umich-edu/caliper-php-public", "public", "e35b0ec"),
                        ("portabilis/i-educar", "2.12", "cd1da68")):
    ok(f"p793/{slug}",
       ref_provenance(row(slug=slug, default_ref=dref, head_sha=sha, served_at=dref))[0],
       "DEFAULT-IS-NEITHER")
ok("p793/served-off-default",
   ref_provenance(row(default_ref="public", served_at="master"))[0], "SERVED-OFF-DEFAULT")
ok("p793/oracle-silent",
   ref_provenance(row(default_ref="-", served_at="master"))[0], "REF-ORACLE-SILENT")

# ---- 5c. the cross-LAYER contradiction this pass found, kept as a named case --------------
# `tl-its-umich-edu/caliper-php-public` @ `refs/heads/public` (`e35b0ec`) — the only reachable
# Caliper Analytics implementation this shelf has found (`Gap 284`):
#   layer 1  `LICENSE`, 7 438 B, title line "GNU LESSER GENERAL PUBLIC LICENSE / Version 3"
#            -> `p419.familia()` says LGPL-3.0, 0 cross-mentions  (p419 self-test 10/10 green)
#   layer 3  `composer.json` -> "license": "proprietary", name `umich-its-tl/caliper-php`
# Two reused instruments, both green, landing in OPPOSITE bands. Neither reading makes the row
# permissive, so `Gap 284` stays open either way — but a pass that reads ONE layer and stops
# would publish a licence this repository contradicts in the other.
CALIPER_FILE_LAYER = "LGPL-3.0"
CALIPER_MANIFEST_LAYER = "proprietary"
ok("caliper/layers-disagree", CALIPER_FILE_LAYER == CALIPER_MANIFEST_LAYER, False)
ok("caliper/neither-is-permissive",
   any(x in ("MIT", "Apache-2.0", "BSD-3-Clause", "BSD-2-Clause")
       for x in (CALIPER_FILE_LAYER, CALIPER_MANIFEST_LAYER)), False)
ok("caliper/ref-is-not-master",
   ref_provenance(row(slug="tl-its-umich-edu/caliper-php-public", default_ref="public",
                      head_sha="e35b0ec", served_at="public"))[0], "DEFAULT-IS-NEITHER")

# ---- 6. REGRESSION, and it is the reset that started this ---------------------------------
# A `000` is a reset, not an answer. It may not produce an absence in ANY of the three verdicts.
RESET = row(slug="a/b", tree_name="v/p", tree_name_http="000", guessed_http="000",
            probe_kind="declared+guessed")
ok("regression/reset-is-not-an-absence", id_provenance(RESET)[0], "AGREES")
ok("regression/reset-no-package-claim", package_identity(RESET)[0] in
   ("UNDETERMINED", "DECLARED-NOT-PUBLISHED"), True)
ok("regression/reset-never-published", package_identity(RESET)[0] != "PUBLISHED-AT-ROOT", True)
# and a reset pair is UNREACHABLE, which is the only honest host line for it
ok("regression/reset-pair-is-unreachable", host_verdict("000", "000")[0], "UNREACHABLE")

# ---- 7. the committed sweep parses and every row carries three verdicts -------------------
try:
    rs = rows_with("result.2026-10-08.tsv")
    ok("sweep/parses", len(rs) > 0, True)
    ok("sweep/every-row-has-three-verdicts",
       all(a[0] and b[0] and c[0] for _, a, b, c in rs), True)
except FileNotFoundError:
    print("  SKIP sweep/* (result.2026-10-08.tsv absent)")

print(f"\n{len(P)}/{len(P) + len(F)} green" + ("" if not F else f" — FAILED: {F}"))
sys.exit(1 if F else 0)
