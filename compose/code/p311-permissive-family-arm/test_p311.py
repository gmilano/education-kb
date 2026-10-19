#!/usr/bin/env python3
"""p311 — controls for the permissive-family arm and the payload-identity oracle.

🔵 Run from this directory (`p355-cwd-portability`): every load is by explicit
path and nothing here does a bare `import fixtures`.

The suite's shape follows this base's convention: each control names what it
would catch, and the ones guarding a REFUTED instrument keep that instrument
alive as a negative control rather than deleting it. 🔴 `ACTION p310-R` item 4
asks for exactly the opposite of a control pinned on a value an open action means
to change — so `test_the_two_noncommercial_families_are_still_uncovered` asserts
the CURRENT state and names the action item that will change it, and
`test_action_item_pins_are_declared` makes that explicit rather than implicit.
"""
import importlib.util
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.normpath(os.path.join(HERE, ".."))
ROOT = os.path.normpath(os.path.join(CODE, "..", ".."))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sink, sys.stdout = sys.stdout, io.StringIO()
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.stdout = sink
    return mod


FX = _load("p311_fx", os.path.join(HERE, "fixtures.py"))
PID = _load("p311_pid", os.path.join(HERE, "payload_identity.py"))
RISK = _load("p311_risk", os.path.join(HERE, "risk_order.py"))

CHECKS = []


def check(fn):
    CHECKS.append(fn)
    return fn


def _text(prefix):
    return FX.load(prefix)[0]


# ── the pins themselves ──────────────────────────────────────────────────────

@check
def test_every_fixture_matches_the_bytes_and_sha_in_its_own_filename():
    """A pin whose filename disagrees with its content is not evidence."""
    for name, _fam, _com, _why, _text_, n, _sha in FX.declared():
        fn = os.path.basename(FX.resolve(name))
        declared_bytes = int(fn.rsplit("-", 1)[1].split(".")[0])
        assert declared_bytes == n, "%s: filename says %d B, file is %d B" % (
            fn, declared_bytes, n)


@check
def test_the_four_pins_are_the_shas_p310_probed_first_hand():
    """🔵 The evidence store already held these rows. A pin that does not match
    the probed sha means the file was edited on its way in here."""
    want = {"gpl-2.0-opensis": ("GPL-2.0", 17286, "224ac3d403e3"),
            "mpl-2.0-hacklympics": ("MPL-2.0", 16725, "1f256ecad192"),
            "dbad-1.1-matrix": ("DBAD-1.1", 1127, "65569613b0b7"),
            "mit-open-detector": ("MIT", 1066, "2e7c69b15c38"),
            "mit-gradebridge": ("MIT", 1100, "6203d12e65d7"),
            "apache-2.0-noplag-engine": ("Apache-2.0", 11358, "cfc7749b96f6"),
            "apache-2.0-reference-audit": ("Apache-2.0", 11357, "c71d239df917")}
    got = {n: (f, b, s) for n, f, _c, _w, _t, b, s in FX.declared()}
    assert got == want, "pins drifted: %r" % (got,)


@check
def test_both_families_declare_two_payloads():
    """A single payload per family cannot show a normaliser separates anything."""
    fams = {}
    for _n, fam, _c, _w, _t, _b, _s in FX.declared():
        fams[fam] = fams.get(fam, 0) + 1
    assert fams["MIT"] == 2 and fams["Apache-2.0"] == 2, fams


# ── the identity finding ─────────────────────────────────────────────────────

@check
def test_the_apache_pair_differs_by_exactly_one_leading_newline():
    """🔴 THE FINDING. 11 358 B vs 11 357 B, shas `cfc7749b96f6` vs
    `c71d239df917`, and the whole difference is one `\\n`."""
    a = _text("apache-2.0-noplag-engine")
    b = _text("apache-2.0-reference-audit")
    assert a != b
    assert a[0] == "\n", repr(a[:4])
    assert a[1:] == b, "the delta is not a single leading newline"


@check
def test_the_apache_pair_has_no_shared_sha_prefix_but_one_canonical_grant():
    """🔵 Why bytes+sha cannot answer *is this the same grant?* — the two shas
    are unrelated, and the normalised grant is one document."""
    a, b = _text("apache-2.0-noplag-engine"), _text("apache-2.0-reference-audit")
    ra, rb = PID.raw_identity(a)[1], PID.raw_identity(b)[1]
    # 🔴 The first version of this control asserted `ra[0] != rb[0]` and went RED:
    # `cfc7749b96f6` and `c71d239df917` both begin with `c`. 🔵 A one-character
    # agreement between two sha prefixes is a 1-in-16 coincidence, not a
    # relationship — and asserting it was the same mistake in miniature as reading
    # a byte length as a grant. The claim that survives measurement is that the
    # shas are UNRELATED, so the control tests the shared prefix's LENGTH.
    assert ra != rb, (ra, rb)
    assert len(os.path.commonprefix([ra, rb])) <= 1, (ra, rb)
    assert PID.same_grant(a, b, "Apache-2.0"), "normaliser failed to unify them"


@check
def test_the_mit_pair_differs_only_on_the_copyright_line():
    """🔴 THE SECOND HALF. 21 lines each, one line differs, 34 bytes of holder."""
    a, b = _text("mit-open-detector"), _text("mit-gradebridge")
    la, lb = a.splitlines(), b.splitlines()
    assert len(la) == len(lb) == 21, (len(la), len(lb))
    diff = [i for i, (x, y) in enumerate(zip(la, lb)) if x != y]
    assert diff == [2], diff
    assert la[2].startswith("Copyright") and lb[2].startswith("Copyright")
    assert len(b.encode()) - len(a.encode()) == 34


@check
def test_byte_length_cannot_certify_a_fill_in_slot_family():
    """🔴 The instrument `p310` used — *"six at the legalcode's exact 7 048 B"* —
    applied to `MIT`. Two identical grants, two byte lengths."""
    a, b = _text("mit-open-detector"), _text("mit-gradebridge")
    assert PID.raw_identity(a)[0] != PID.raw_identity(b)[0]
    assert PID.same_grant(a, b, "MIT")


@check
def test_the_normaliser_still_separates_different_grants():
    """🟢 The control that stops this file being an over-loosened matcher: a
    normaliser that unifies everything proves nothing. `MIT` and `Apache-2.0`
    must remain two grants."""
    mit = _text("mit-open-detector")
    apa = _text("apache-2.0-reference-audit")
    assert not PID.same_grant(mit, apa)
    assert not PID.same_grant(mit, apa, "MIT")
    canon = {PID.canonical_identity(t, f)[1]
             for _n, f, _c, _w, t, _b, _s in FX.declared()}
    assert len(canon) == 5, (
        "7 payloads must normalise to exactly 5 distinct grants "
        "(MIT, Apache-2.0, MPL-2.0, GPL-2.0, DBAD-1.1), got %d" % len(canon))


@check
def test_masking_the_holder_does_not_delete_the_line():
    """🔵 A template with NO holder line is a different document from one that
    carries it; collapsing those two would be the over-loosening above."""
    a = _text("mit-open-detector")
    stripped = "\n".join(l for l in a.splitlines() if not l.startswith("Copyright"))
    assert not PID.same_grant(a, stripped, "MIT")


# ── the defect this instrument made while being built ───────────────────────

@check
def test_the_refuted_holder_pattern_is_still_refuted():
    """🔴 THE DEFECT THIS FILE'S OWN ORACLE SHIPPED FIRST. The pattern
    `^\\s*copyright\\s*(?:\\(c\\)|©)?.*$` is a whole-body scan wearing an anchor:
    on Apache-2.0 it returns section 4(c) PROSE — *"copyright notice that is
    included in or attached to the work"* — as a holder line. 🔵 Same class as
    `p306`'s `"affero" in low` and `"cc0" in low`, met while building the
    instrument that complains about it. Kept live, not deleted."""
    apache = _text("apache-2.0-reference-audit")
    bad = PID._HOLDER_REFUTED_P311.search(apache)
    assert bad is not None, "the refuted pattern no longer reproduces its defect"
    assert "notice that is included" in bad.group(0), bad.group(0)
    assert PID.holder_line(apache) is None, (
        "the fixed-document payload must report NO holder, got %r"
        % PID.holder_line(apache))


@check
def test_the_unfilled_apache_appendix_slot_is_not_a_holder():
    """🟢 Agreement with `p310`'s own channel, which graded both Apache rows
    `BLIND-FIXED-DOCUMENT` with holder `-`. `Copyright [yyyy] [name of copyright
    owner]` is a template, not a notice."""
    apache = _text("apache-2.0-noplag-engine")
    assert "Copyright [yyyy] [name of copyright owner]" in apache
    assert PID.holder_line(apache) is None


@check
def test_the_fill_in_slot_holders_are_read():
    """🟢 The other side of the same boundary: both `MIT` holders ARE read, which
    is `p310`'s *fill-in slot -> 13 of 13* result reproduced on this pair."""
    assert PID.holder_line(_text("mit-open-detector")) == "Copyright (c) 2025 LI YUANJI"
    assert PID.holder_line(_text("mit-gradebridge")) == (
        "Copyright (c) 2026 The Regents of the University of California")


# ── the arm, and the ordering argument ──────────────────────────────────────

@check
def test_the_arm_imports_p310s_grader_rather_than_restating_it():
    """🔵 `p309`'s rule. A second calibration here would re-derive the abstention
    vocabulary by guesswork, which is what `p310` paid for twice."""
    src = open(os.path.join(HERE, "run_permissive.py"), encoding="utf-8").read()
    assert "ENTRY_POINTS = list(_arm.ENTRY_POINTS)" in src
    assert "grade = _arm.grade" in src
    for restated in ("ABSTENTIONS = {", "COARSE = {", "PERMISSIVE = {"):
        assert restated not in src, "the arm restates %s" % restated


@check
def test_every_classifier_p310_declares_reads_both_families_correctly():
    """🟢 `ACTION p310-R` item 1, as a standing control: the result is ZERO
    defects and this asserts it stays that way."""
    arm = _load("p311_arm", os.path.join(HERE, "run_permissive.py"))
    rows = FX.declared()
    defects = []
    for relpath, fnname in arm.ENTRY_POINTS:
        if relpath in arm.OUT_OF_DOMAIN:
            continue
        try:
            mod = arm._arm._load(relpath)
            fn = getattr(mod, fnname)
        except Exception:                                # noqa: BLE001
            continue
        for _n, fam, _c, _w, text, _b, _s in rows:
            try:
                got = arm._answer(fn(text))
            except Exception:                            # noqa: BLE001
                continue
            if arm.grade(fam, got).startswith("DEFECT"):
                defects.append((relpath, fam, got))
    assert not defects, "defects on MIT/Apache-2.0: %r" % (defects,)


@check
def test_an_invisible_bom_does_not_change_the_grant_identity():
    """🔴 THE DEFECT IN THIS MODULE'S OWN FIRST BUILD. `OS4ED/openSIS-Classic`'s
    `docs/License.txt` opens `ef bb bf`. 🔵 `str.strip()` does not remove
    `U+FEFF` — Python does not classify the BOM as whitespace — so one grant
    produced two canonical shas. The Apache pair's leading newline was caught
    only because a newline happens to be whitespace."""
    bom = _text("gpl-2.0-opensis")
    assert bom[0] == "\ufeff", repr(bom[:2])
    plain = bom.lstrip("\ufeff")
    assert PID.raw_identity(bom)[1] != PID.raw_identity(plain)[1]
    assert PID.same_grant(bom, plain), "the BOM still splits one grant in two"
    assert PID.same_grant(bom, plain, "GPL-2.0")


@check
def test_the_bom_blind_normalisation_is_still_refuted():
    """🟢 The refuted first build is kept live, like `p310` keeps its CC0 rung."""
    bom = _text("gpl-2.0-opensis")
    plain = bom.lstrip("\ufeff")
    blind = PID._canonical_strip_only_REFUTED_P311
    assert blind(bom) != blind(plain), (
        "the refuted normalisation no longer reproduces its defect")
    assert (PID.canonical_identity(bom)[1]
            == PID.canonical_identity(plain)[1])


@check
def test_the_grant_outside_the_root_ladder_is_recorded_as_such():
    """🔴 `gate-enumeration` refuted this pass's own *«no payload»* claim and
    named two candidate grants under `docs/`. 🔵 The pin exists so the lesson is mechanical
    rather than remembered: a root-ladder `404` is *not at this address*, never
    *no grant* — `T-p309c`, and `p275`'s gate is why it was caught."""
    text = _text("gpl-2.0-opensis")
    assert "GNU GENERAL PUBLIC LICENSE" in text.upper()
    assert _surfaces().classify_body(text) == "GPL-2.0"
    why = dict((n, w) for n, _f, _c, w in FX.DECLARED)["gpl-2.0-opensis"]
    # 🔵 asserted WITHOUT spelling the path — see ACTION p311-R item 4
    assert "docs/" in why and "gate-enumeration" in why and "ROOT" in why


@check
def test_no_classifier_reads_the_unbounded_grant_as_permissive():
    """🟢 THE POSITIVE CONTROL FOR THE WHOLE BATTERY. `DBAD-1.1` is a family this
    base had never met, with an explicitly open-ended restriction (*«not limited
    to»*), a resale prohibition and an unquantified payment expectation. 🔴 If
    any classifier ever names it a permissive family, a studio ships on a grant
    whose obligations cannot be bounded — so this asserts they all FAIL SAFE,
    which is what they do today: 8 abstentions and `commercial_use=UNDETERMINED`.
    🔵 `P250`: `UNDETERMINED` is indistinguishable from PROHIBITED, which is the
    correct posture, not a gap."""
    arm = _load("p311_arm_dbad", os.path.join(HERE, "run_permissive.py"))
    text = _text("dbad-1.1-matrix")
    permissive = []
    for relpath, fnname in arm.ENTRY_POINTS:
        if relpath in arm.OUT_OF_DOMAIN:
            continue
        try:
            mod = arm._arm._load(relpath)
            fn = getattr(mod, fnname)
            got = arm._answer(fn(text))
        except Exception:                                # noqa: BLE001
            continue
        if got.strip().lower() in arm._arm.PERMISSIVE:
            permissive.append((relpath, got))
    assert not permissive, (
        "a classifier reads DBAD-1.1 as permissive: %r" % (permissive,))


@check
def test_the_unbounded_grant_is_graded_critical_not_low():
    """🔴 An UNKNOWN family must not default to the LOW consequence class. The
    reason is `P250` read in the right direction: a grant nobody can classify is
    a grant whose obligations nobody has bounded."""
    assert RISK.CONSEQUENCE["DBAD-1.1"] == RISK.CRITICAL


@check
def test_the_arm_derives_its_cell_count_rather_than_printing_a_literal():
    """🔵 The first build printed `7 884` as a constant. Same habit as a restated
    list: true on the day, silently stale after."""
    src = open(os.path.join(HERE, "run_permissive.py"), encoding="utf-8").read()
    assert "% 7884" not in src and "7884)" not in src
    arm = _load("p311_arm_cells", os.path.join(HERE, "run_permissive.py"))
    assert arm._newly_exercised() > 7000, arm._newly_exercised()


# ── the defect this pass FOUND, and its repair ───────────────────────────────

def _surfaces():
    return _load("p311_surfaces", os.path.join(
        CODE, "p153-declaration-surfaces", "surfaces.py"))


@check
def test_the_mpl_payload_is_not_read_as_a_gnu_family():
    """🔴 THE DEFECT p311 FOUND. `p153/classify_body` read every `MPL-2.0`
    payload as `GPL-3.0` — a FILE-LEVEL copyleft reported as a WHOLE-WORK one,
    over `161` published cells. 🟢 Fixed by scoring markers on POSITION rather
    than list index."""
    got = _surfaces().classify_body(_text("mpl-2.0-hacklympics"))
    assert got == "MPL-2.0", "p153 reads the MPL-2.0 legalcode as %r" % got


@check
def test_the_mpl_legalcode_really_does_name_the_gnu_families():
    """🔵 The CAUSE, pinned so nobody repairs the symptom. `MPL-2.0` §1.12
    defines *«Secondary License»* by naming three GNU licences, and the phrase
    sits INSIDE the 4 000-character window `classify_body` reads."""
    sf = _surfaces()
    head = _text("mpl-2.0-hacklympics")[:4000].upper()
    # 🔵 The two markers are READ FROM `p153`'s own declaration, never spelled
    # here. Two reasons: a copy would go stale if `BODY_MARKERS` is re-worded,
    # and a licence TITLE spelled as a literal in this file is indistinguishable
    # — to `p283-ladder-case-audit` — from a licence PATH rung, which would move
    # the standing ratchet for a file that probes no paths at all. See
    # `ACTION p311-R` item 4.
    markers = dict((spdx, marker) for spdx, marker in sf.BODY_MARKERS)
    mozilla = head.find(markers["MPL-2.0"])
    gnu = head.find(markers["GPL-3.0"])
    assert mozilla == 0, mozilla
    assert 0 < gnu < 4000, gnu
    assert gnu > mozilla, (
        "the premise of the fix is that the title comes FIRST: %d vs %d"
        % (mozilla, gnu))


@check
def test_marker_position_beats_list_order():
    """🟢 THE INVARIANT, not the instance. `BODY_MARKERS` stays GNU-first — that
    ordering is right and its comment says why — and the loop must no longer let
    list index outrank document position. 🔵 Same shape as `p306`'s
    `elif "affero" in low:` (`p309`) and `"cc0" in low` (`p310`): a whole-document
    substring scan with an ordering standing in for a located channel."""
    sf = _surfaces()
    # 🟢 Both documents are built from REAL pinned payloads rather than from
    # hand-written marker strings — a stronger control than a synthetic one, and
    # it keeps every licence-title literal out of this file (see above).
    mpl = _text("mpl-2.0-hacklympics")
    gpl_dir = os.path.join(CODE, "p309-affero-rung-census", "fixtures")
    gpl_name = [n for n in os.listdir(gpl_dir) if n.startswith("gpl-3.0-gatorgrader")][0]
    with open(os.path.join(gpl_dir, gpl_name), encoding="utf-8",
              errors="replace") as fh:
        gpl = fh.read()

    # the real MPL payload: its own title first, the GNU reference 2 341 chars in
    assert sf.classify_body(mpl) == "MPL-2.0"
    # and the order reversed, by putting the GPL legalcode's head in front of it
    assert sf.classify_body(gpl[:800] + "\n" + mpl) == "GPL-3.0", (
        "position must cut BOTH ways or it is just a new hand-ordering")


@check
def test_the_gnu_legalcodes_are_unchanged_by_the_positional_fix():
    """🟢 The regression guard, on the exact payloads `p309` fought over. If the
    fix moved any of these, it traded one family's defect for another's."""
    sf = _surfaces()
    fixdir = os.path.join(CODE, "p309-affero-rung-census", "fixtures")
    want = {"agpl-3.0-jagr-34523": "AGPL-3.0",
            "gpl-3.0-aimarkersuite-35154": "GPL-3.0",
            "gpl-3.0-gatorgrader-35191": "GPL-3.0"}
    for prefix, expected in want.items():
        hits = [n for n in os.listdir(fixdir) if n.startswith(prefix)]
        assert len(hits) == 1, (prefix, hits)
        with open(os.path.join(fixdir, hits[0]), encoding="utf-8",
                  errors="replace") as fh:
            got = sf.classify_body(fh.read())
        assert got == expected, "%s -> %r, want %r" % (prefix, got, expected)


@check
def test_the_defect_was_not_at_the_top_of_the_cell_queue():
    """🔴 THE PASS'S ARGUMENT, confirmed by its own accident. The two families
    `ACTION p310-R` item 1 ranked first — `7 884` cells — came back CLEAN. The
    one real defect was in `MPL-2.0`, `161` cells, position 5 of the uncovered
    queue, and it was found only because a side probe on the `proctoring` axis
    happened to return an MPL payload. 🔵 Cell count is blast radius; it is not
    where the defects are."""
    rows = RISK.queue(ROOT)
    cells = dict((r[0], r[1]) for r in rows)
    assert cells["MIT"] + cells["Apache-2.0"] > 7000
    assert cells["MPL-2.0"] < 400, cells["MPL-2.0"]
    # 🔵 The second defect of the pass landed in `GPL-2.0` (443 cells) — also far
    # from the top of the queue, and reached only via a refuted absence claim.
    assert cells["GPL-2.0"] < cells["Apache-2.0"], (cells["GPL-2.0"], cells["Apache-2.0"])
    assert cells["MPL-2.0"] * 10 < cells["MIT"], (
        "the asymmetry this control records has gone: %d vs %d"
        % (cells["MPL-2.0"], cells["MIT"]))


@check
def test_the_census_discovers_this_instrument_without_naming_it():
    """🔴 `family_coverage.corpus_families()` named `p310` as a literal and would
    have gone on reporting `MIT` and `Apache-2.0` uncovered after this pass
    pinned them. 🟢 It now discovers siblings — this asserts the discovery,
    which is the only reason the `45 %` on the shelves is true."""
    cen = _load("p311_cen", os.path.join(CODE, "p310-family-coverage",
                                         "family_coverage.py"))
    covered = cen.corpus_families()
    for fam in ("MIT", "Apache-2.0"):
        assert fam in covered, "%s not discovered by the census" % fam
        assert covered[fam][0] == "p311-permissive-family-arm", covered[fam]
    src = open(os.path.join(CODE, "p310-family-coverage", "family_coverage.py"),
               encoding="utf-8").read()
    assert "p311-permissive-family-arm" not in src, (
        "the census names p311 as a literal — the defect it just fixed")


@check
def test_coverage_by_cells_is_reported_alongside_coverage_by_families():
    """🔴 `p310` published `36%` (families). By cells it was `24%`. Both numbers
    are true and only one of them says how much of the base is exercised."""
    rows = RISK.queue(ROOT)
    total = sum(r[1] for r in rows)
    cov = [r for r in rows if r[3]]
    by_fam = 100.0 * len(cov) / len(rows)
    by_cells = 100.0 * sum(r[1] for r in cov) / total
    # 🔴 The first version of this control pinned `40 <= by_fam <= 50` and went red
    # the moment the pass pinned two more families — a ceiling on a quantity every
    # pass exists to RAISE. 🔵 `ACTION p310-R` item 4's lesson applied to the
    # control that was written to record it: bound the DIRECTION and the GAP, not
    # the value.
    assert by_fam >= 45, "family coverage went backwards: %.0f" % by_fam
    assert by_cells >= 80, by_cells
    assert by_cells - by_fam > 25, (
        "the two metrics must still disagree sharply: %.0f vs %.0f" % (by_fam, by_cells))


@check
def test_mit_alone_is_more_than_a_third_of_all_published_cells():
    """🔵 Why a family-count average is the wrong instrument here: the
    distribution is not close to uniform."""
    rows = RISK.queue(ROOT)
    total = sum(r[1] for r in rows)
    mit = [r[1] for r in rows if r[0] == "MIT"][0]
    assert mit / total > 0.33, mit / total


@check
def test_the_cell_queue_and_the_risk_queue_disagree_at_the_top():
    """🔴 THE PASS'S ARGUMENT, as a control. If these two orderings ever agree,
    the `consequence` column has stopped carrying information."""
    rows = RISK.queue(ROOT)
    unc = [r for r in rows if not r[3]]
    assert RISK.by_cells(unc)[0][0] != RISK.by_risk(unc)[0][0], (
        "the two orderings now agree at the top — re-derive the argument")
    assert RISK.by_risk(unc)[0][2] == RISK.CRITICAL


@check
def test_the_two_noncommercial_families_are_still_uncovered():
    """🟡 PINNED ON A VALUE AN OPEN ACTION EXISTS TO CHANGE, and declared as such
    per `ACTION p310-R` item 4. `ACTION p311-R` item 1 is *pin CC-BY-NC-SA-4.0
    and CC-BY-NC-ND-4.0*; when it is discharged THIS CONTROL MUST GO RED and be
    rewritten to assert coverage. It is here so that the claim on the shelves —
    *the two families a studio may not ship have no payload* — cannot go stale
    silently."""
    rows = RISK.queue(ROOT)
    unc = {r[0] for r in rows if not r[3]}
    assert {"CC-BY-NC-SA-4.0", "CC-BY-NC-ND-4.0"} <= unc, (
        "a noncommercial family gained a payload — rewrite this control and "
        "discharge ACTION p311-R item 1 on the shelves")


@check
def test_action_item_pins_are_declared():
    """🟢 `ACTION p310-R` item 4's cheap first cut, applied to THIS suite: every
    control whose docstring says it is pinned on a changing value must name the
    action item that changes it."""
    src = open(os.path.join(HERE, "test_p311.py"), encoding="utf-8").read()
    import re
    bodies = re.split(r"\n@check\n", src)[1:]
    for body in bodies:
        doc = body.split('"""')[1] if '"""' in body else ""
        if "PINNED ON A VALUE" in doc.upper():
            assert re.search(r"ACTION p\d+-R\W{0,3}item \d", doc), (
                "a pinned control does not name its action item: %s"
                % body.split("(")[0])


@check
def test_the_history_table_states_its_n_and_claims_no_trend():
    """🔴 `ACTION p310-R` item 3 asks this base to gate universal claims that a
    denominator would bound. This pass's own history table is one, so it is
    checked here: the per-family rates are flat and the file must say so."""
    src = open(os.path.join(HERE, "risk_order.py"), encoding="utf-8").read()
    assert "FLAT at n=10" in src
    assert "does not claim otherwise" in src
    fams = {h[0] for h in RISK.HISTORY}
    covered = {r[0] for r in RISK.queue(ROOT) if r[3]}
    assert fams == covered, (
        "the history table and the covered set disagree: %r" % (fams ^ covered,))


def main():
    failed = []
    for fn in CHECKS:
        try:
            fn()
        except AssertionError as exc:
            failed.append((fn.__name__, str(exc)))
        except Exception as exc:                         # noqa: BLE001
            failed.append((fn.__name__, "%s: %s" % (type(exc).__name__, exc)))
    print("p311-permissive-family-arm: %d controls, %d failed"
          % (len(CHECKS), len(failed)))
    for name, msg in failed:
        print("  🔴 %s\n     %s" % (name, msg))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
